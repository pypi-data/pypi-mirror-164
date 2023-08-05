import os
import re
import shutil
import warnings
from ast import literal_eval
from textwrap import dedent
from typing import Any, Callable, Optional, Type, Union

import yaml
from omegaconf import DictConfig, OmegaConf


def clean_multiline(string: str) -> str:
    string = dedent(string.strip())
    string = re.sub(r"\s*\n\s*", " ", string)
    return string


class PrintUtils:
    """A few utilities to make printing easier"""

    def __init__(
        self,
        indent_step: int = 2,
        indent_char: str = " ",
        separator_char: str = "-",
        terminal_width: Optional[int] = None,
        print_fn: Optional[Callable[..., None]] = None,
    ) -> None:
        self.indent_step = indent_step
        self.indent_char = indent_char
        self.separator_char = separator_char
        self.terminal_width = (
            terminal_width or shutil.get_terminal_size().columns
        )
        self.print_fn = print_fn or print
        self.has_printed_first_separator = False
        self.is_default_print = self.print_fn is print

    def print(
        self,
        *lines: Union[str, dict, DictConfig],
        level: int = 0,
        level_up: Optional[int] = None,
    ):

        level_up = level_up or float("inf")  # type: ignore

        content = ""
        if self.is_default_print:
            if not self.has_printed_first_separator:
                content += self.separator()
            self.has_printed_first_separator = True

        for line in lines:
            if not line:
                # backtrack the new line you just added from previous
                # argument if the current argument evaluates to none, like
                # an empty string, or an empty dict
                content = f"{content.rstrip()} "

            if isinstance(line, DictConfig):
                # we ignore type bc we are ok with line being any of
                # the types returned by omegaconf
                line = OmegaConf.to_container(line)  # type: ignore

            if isinstance(line, dict):
                content += f"{self.to_yaml(line, level)}\n"
            else:
                content += f"{self.indent(str(line), level)}\n"

            level += 1 if level < level_up else 0  # type: ignore

        if self.is_default_print:
            content += f"{self.separator()}\n"

        self.print_fn(content.rstrip())  # type: ignore

    def indent(self, line: str, level: int) -> str:
        indent = self.indent_char * level * self.indent_step
        return indent + line

    def separator(self, level: int = 0) -> str:
        separator = self.separator_char * self.terminal_width
        return self.indent(separator, level=level)

    def to_yaml(self, content: dict, level: int = 0) -> str:
        if not content:
            # this is in case the dict/list is empty
            return str(content)

        out = yaml.dump(
            content,
            indent=self.indent_step,
            width=self.terminal_width,
            default_flow_style=False,
        )
        out = "\n".join(
            self.indent(ln, level) for ln in out.strip().split("\n")
        ).rstrip()
        return out


class SpringsWarnings:
    _WARNINGS = literal_eval(os.environ.get("SPRINGS_WARNINGS", "True"))

    @classmethod
    def toggle(cls, value: Optional[bool] = None):
        if value is None:
            value = not cls._WARNINGS
        cls._WARNINGS = value

    @classmethod
    def _warn(
        cls: Type["SpringsWarnings"],
        message: str,
        category: Type[Warning],
        stacklevel: int = 2,
    ):
        if cls._WARNINGS:
            warnings.warn(message, category, stacklevel=stacklevel)

    @classmethod
    def missing_type(cls: Type["SpringsWarnings"], fn_name: str, type_: Any):
        if type_ is None:
            cls._warn(
                clean_multiline(
                    f"""It is strongly recommended to provide a _type_ argument
                        to `{fn_name}`. This ensures that the correct type is
                        annotated as the return value. Further, it performs
                        type checking on the initialized object."""
                ),
                category=UserWarning,
            )

    @classmethod
    def flexyclass(cls: Type["SpringsWarnings"]):
        cls._warn(
            clean_multiline(
                """Decorating with `flexyclass` is discouraged because it
                   does not play nicely with mypy, resulting in incorrect
                   type annotations. Instead, consider decorating with
                   `@springs.dataclass` first, and then decorating
                   `@springs.make_flexy` on the resulting class."""
            ),
            category=UserWarning,
        )

    @classmethod
    def flexyfield(cls: Type["SpringsWarnings"]):
        cls._warn(
            clean_multiline(
                """`flexy_field` is provided as a convenience for passing
                values that are not explicitly annotated for a flexyclass;
                however, it is not recommended because it not very pythonic.
                Instead, creating an flexyclass that inherits from the current
                one with the desired field and default value. Non explicit
                values are expected to be provided at runtime. """
            ),
            category=UserWarning,
        )

    @classmethod
    def argument(cls: Type["SpringsWarnings"], arg_name: str, obj_name: str):
        cls._warn(
            f"'{arg_name}' was provided to `{obj_name}`, but it is ignored",
            category=SyntaxWarning,
        )
