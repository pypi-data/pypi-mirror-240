import types
from inspect import FrameInfo, currentframe, getouterframes
from typing import Union

from langchain.output_parsers import PydanticOutputParser
from langchain.schema import BaseOutputParser, StrOutputParser

from funcchain.parser import BoolOutputParser, ParserBaseModel


def get_parent_frame(depth: int = 5) -> FrameInfo:
    return getouterframes(currentframe())[depth]


def from_docstring() -> str:
    """
    Get the docstring of the parent caller function.
    """
    doc_str = (caller_frame := get_parent_frame()).frame.f_globals[caller_frame.function].__doc__
    return "\n".join([line.lstrip() for line in doc_str.split("\n")])


def get_output_type() -> type:
    """
    Get the output type annotation of the parent caller function.
    """
    try:
        return (caller_frame := get_parent_frame()).frame.f_globals[caller_frame.function].__annotations__["return"]
    except KeyError:
        raise ValueError("The funcchain must have a return type annotation")


def parser_for(output_type: type) -> BaseOutputParser | None:
    """
    Get the parser from the type annotation of the parent caller function.
    """
    if isinstance(output_type, types.UnionType):
        return None
    if getattr(output_type, "__origin__", None) is Union:
        output_type = output_type.__args__[0]  # type: ignore
        return None
    if output_type is str:
        return StrOutputParser()
    if output_type is bool:
        return BoolOutputParser()
    if issubclass(output_type, ParserBaseModel):
        return output_type.output_parser()
    from langchain.pydantic_v1 import BaseModel

    if issubclass(output_type, BaseModel):
        return PydanticOutputParser(pydantic_object=output_type)
    # TODO: Add support for Union without function calling
    # if getattr(output_type, "__origin__", None) is Union:
    #     return MultiPydanticOutputParser(pydantic_objects=output_type.__args__)
    else:
        raise NotImplementedError(f"Unknown output type: {output_type}")


def kwargs_from_parent() -> dict[str, str]:
    """
    Get the kwargs from the parent function.
    """
    return get_parent_frame().frame.f_locals
