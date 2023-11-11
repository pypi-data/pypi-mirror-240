from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def formatted(func: Callable[P, str]) -> Callable[P, str]:
    """Decorater that takes str returned from function and removes leading spaces from each lines"""

    def formatted_wrapper(*args: P.args, **kwargs: P.kwargs) -> str:
        result = func(*args, **kwargs).lstrip("\n")
        min_tab = min(
            _count_leading_spaces(line) for line in result.split("\n") if line and line.count(" ") < len(line)
        )
        lines = (line[min_tab:] for line in result.split("\n"))
        return "\n".join(lines)

    return formatted_wrapper


def _count_leading_spaces(input_str: str) -> int:
    spaces = 0
    for char in input_str:
        if not char.isspace():
            break
        spaces += 1
    return spaces
