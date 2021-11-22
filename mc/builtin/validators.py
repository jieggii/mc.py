from typing import Optional

from mc.types import Validator


def words_count(minimal: Optional[int] = None, maximal: Optional[int] = None) -> Validator:
    if minimal is None and maximal is None:
        raise ValueError("`minimal` and `maximal` can't be both unspecified.")

    if not minimal:
        minimal = 0

    if not maximal:
        maximal = float("inf")

    def validator(phrase: str) -> bool:
        return minimal <= len(phrase.split()) <= maximal

    return validator


def chars_count(minimal: int = None, maximal: int = None) -> Validator:
    if minimal is None and maximal is None:
        raise ValueError("`minimal` and `maximal` can't be both unspecified.")

    if not minimal:
        minimal = 0

    if not maximal:
        maximal = float("inf")

    def validator(phrase: str) -> bool:
        return minimal <= len(phrase) <= maximal

    return validator
