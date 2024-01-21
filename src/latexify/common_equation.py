from typing import Optional

import latexify as lt
from latexify import config as cfg

from src.latexify import exceptions, Style


def common_equation(
        equation: str,
        symbols: list[str],
        *,
        style: Style = Style.FUNCTION,
        config: Optional[cfg.Config] = None,
        **kwargs,
) -> str:
    """
    Args:
        equation:A common equation to change into latex
        symbols:The equation's symbol
        style: Style of the LaTeX description, the default is FUNCTION.
        config: Use defined Config object, if it is None, it will be automatic assigned
            with default value.
        **kwargs: Dict of Config field values that could be defined individually
            by users.

    Return:
        Generated LaTeX description.

    Raise:
        latexify.exceptions.LatexifyError: Something went wrong during conversion.
        latexify.exceptions.LatexifySyntaxError: The code syntax error
    """
    symbol_text = ""
    lists = []
    for i in symbols:
        symbol_text = "{},".format(i)
        if i not in equation:
            raise exceptions.LatexifySyntaxError("Symbols not in equation.")

    if "=" in equation:
        _text = equation.split("=")
        for equ in _text:
            code = "return {}".format(symbol_text, _text)
            lists.append(lt.get_latex_with_code(name="f", args=symbol_text, code=code, style=style, config=config))
    else:
        _text = equation
        code = "return {}".format(symbol_text, _text)
        lists.append(lt.get_latex_with_code(name="f", args=symbol_text, code=code, style=style, config=config))

    if len(lists) == 1:
        lists[0].replace("f(x) = ", "")
        return lists[0]
    elif len(lists) == 2:
        result = lists[0].replace("f(x) = ", "") + " = " + lists[1].replace("f(x) = ", "")
        return result
    else:
        raise exceptions.LatexifySyntaxError("Too many equations")
