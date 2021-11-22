from typing import Callable

Validator = Callable[[str], bool]
Formatter = Callable[[str], str]
