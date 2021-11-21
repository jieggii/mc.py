from typing import Callable, Optional


def words_count(
    minimal: Optional[int] = None, maximal: Optional[int] = None
) -> Callable[[str], bool]:
    if minimal is None and maximal is None:
        raise ValueError("minimal and maximal can't be both None")

    if not minimal:
        minimal = 0

    if not maximal:
        maximal = float("inf")

    return lambda phrase: minimal <= len(phrase.split()) <= maximal


def chars_count(minimal: int = None, maximal: int = None) -> Callable[[str], bool]:
    if minimal is None and maximal is None:
        raise ValueError("minimal and maximal can't be both unspecified")

    if not minimal:
        minimal = 0

    if not maximal:
        maximal = float("inf")

    return lambda phrase: minimal <= len(phrase) <= maximal
