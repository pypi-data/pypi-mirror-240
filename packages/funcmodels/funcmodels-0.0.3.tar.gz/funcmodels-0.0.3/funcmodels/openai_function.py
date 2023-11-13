from __future__ import annotations
import json
import inspect
import textwrap
import docstring_parser
from typing import (
    Self,
    get_type_hints,
    Callable,
    Any,
    TypeVar,
    Generic,
    cast,
    overload,
    ClassVar,
    Literal,
)
from pydantic import (
    BaseModel,
    create_model,
    Field,
)

ReturnType = TypeVar("ReturnType", covariant=True)


class OpenaiFunction(BaseModel, Generic[ReturnType]):
    schema: ClassVar[dict[str, object]]

    def __init__(self, **_: Any):
        ...

    @property
    def function(self) -> Callable[..., ReturnType]:
        ...

    def __call__(self) -> ReturnType:
        ...

    @classmethod
    def from_json(cls, arguments: str) -> Self:
        ...


@overload
def openai_function(
    __func: Callable[..., ReturnType], /,
) -> type[OpenaiFunction[ReturnType]]:
    ...


@overload
def openai_function(
    __func: None = None, /, 
) -> Callable[[Callable[..., ReturnType]], type[OpenaiFunction[ReturnType]]]:
    ...


def openai_function(
    __func: None | Callable[..., ReturnType] = None, /,
) -> (
    type[OpenaiFunction[ReturnType]]
    | Callable[[Callable[..., ReturnType]], type[OpenaiFunction[ReturnType]]]
):
    def decorator(fn):
        # Get annotations from get_type_hints() since it evaluates forward references.
        # Get defaults and names from inspect.signature() since it includes all of them.
        # Replace empty defaults with `...` since that's what Pydantic expects.

        param_types = get_type_hints(fn)

        param_defaults = {
            name: param.default if param.default is not param.empty else ...
            for name, param in inspect.signature(fn).parameters.items()
        }

        param_names = list(param_defaults.keys())
        assert 'schema' not in param_names, "schema is a reserved parameter name"
        assert 'function' not in param_names, "function is a reserved parameter name"

        model_fields: dict[str, Any] = {
            name: (param_types.get(name, Any), param_defaults[name]) for name in param_names
        }

        cls_name = fn.__name__

        Base = create_model(cls_name, **model_fields)
        function_schema = get_schema(fn, Base)


        class BaseMeta(type(Base)):
            def __repr__(self):
                return f"OpenaiFunction({json.dumps(function_schema, indent=4)})"


        class Model(Base, metaclass=BaseMeta):
            schema: ClassVar[dict[str, object]] = function_schema

            def __call__(self):
                return fn(**self.model_dump())

            @property
            def function(self) -> Callable[..., ReturnType]:
                return fn

            @classmethod
            def from_json(cls, arguments: str) -> Self:
                parsed = json.loads(arguments)
                return cls(**parsed)


        Model.__name__ = cls_name
        return cast(type[OpenaiFunction[ReturnType]], Model)

    if __func is None:
        return decorator  # type: ignore

    return decorator(__func)


def get_schema(fn: Callable, model: type[BaseModel]) -> dict[str, object]:
    schema: dict[str, object] = {
        "name": fn.__name__,
    }
    parameters = model.model_json_schema()
    parameters.pop('title')
    parameters = remove_key_recursive(parameters, 'title')
    schema["parameters"] = parameters

    raw_docstring = fn.__doc__
    if not raw_docstring:
        return schema

    docstring = textwrap.dedent(raw_docstring).strip()

    doc = docstring_parser.parse(docstring)

    if doc.params:
        descriptions = {
            param.arg_name: param.description for param in doc.params
            if param.description and param.arg_name
            and param.arg_name in parameters['properties']
        }
        for name, description in descriptions.items():
            schema['parameters']['properties'][name]['description'] = description

    docstring_without_params = remove_parameters_section_from_docstring(docstring).strip()
    if not docstring_without_params:
        return schema

    schema["description"] = docstring_without_params

    # Re-order keys so description is first. Better readability.
    return {
        "name": schema["name"],
        "description": schema["description"],
        "parameters": schema["parameters"],
    }


def remove_key_recursive(item, key_to_remove) -> Any:
    if isinstance(item, dict):
        return {
            key: remove_key_recursive(value, key_to_remove)
            for key, value in item.items()
            if key != key_to_remove
        }
    elif isinstance(item, (list, tuple)):
        return [remove_key_recursive(value, key_to_remove) for value in item]
    else:
        return item


def remove_parameters_section_from_docstring(docstring: str) -> str:
    numpydoc_sections = {"Parameters", "Returns", "Examples", "Raises", "Notes", "References", "Yields"}
    lines = docstring.split("\n")
    params_start = None
    params_end = len(lines)

    for i, line in enumerate(lines):
        if line.strip() == 'Parameters':
            params_start = i
            continue

        if params_start != -1 and any(line.strip() == section for section in numpydoc_sections):
            params_end = i
            break

    if params_start is None:
        return docstring

    new_lines = lines[:params_start] + lines[params_end:]
    return '\n'.join(new_lines)


if __name__ == "__main__":

    @openai_function
    def get_stock_price(ticker: str, currency: Literal["USD", "EUR"] = "USD"):
        """
        Get the stock price of a company, by ticker symbol

        Parameters
        ----------
        ticker
            The ticker symbol of the company
        currency
            The currency to use
        """
        return f"182.41 {currency}, -0.48 (0.26%) today"

    print(issubclass(get_stock_price, BaseModel))
    print(repr(get_stock_price))

    openai_args = '{"ticker": "AAPL"}'

    model = get_stock_price.from_json(openai_args)
    print(repr(model))
    result = model()
    print(result)
    print("_--------------")

    @openai_function
    def get_stock_price(
        ticker: str = Field(description="The ticker symbol of the company"),
        currency: Literal["USD", "EUR"] = Field(default="USD", description="The currency to use"),
    ):
        """
        Get the stock price of a company, by ticker symbol
        """
        return f"182.41 {currency}, -0.48 (0.26%) today"


    print(repr(get_stock_price))

    openai_args = '{"ticker": "AAPL"}'

    model = get_stock_price.from_json(openai_args)
    print(repr(model))
    result = model()
    print(result)











