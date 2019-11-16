# todo: add more validators
from mc import exceptions
import typing


def default(_) -> bool:
    return True


def combine(*args: typing.Callable) -> typing.Callable:
    def combined_validator(phrase: str) -> bool:
        for validator in args:
            if not validator(phrase):
                return False

        return True

    return combined_validator


def words_count(minimal: int = None, maximal: int = None) -> typing.Callable:
    if not minimal and not maximal:
        raise exceptions.ValidatorError("minimal and maximal can't be unset both")

    if not minimal:
        minimal = 0

    if not maximal:
        maximal = float("inf")

    return lambda phrase: minimal <= len(phrase.split(" ")) <= maximal


def symbols_count(minimal: int = None, maximal: int = None) -> typing.Callable:
    if not minimal and not maximal:
        raise exceptions.ValidatorError("minimal and maximal can't be unset both")

    if not minimal:
        minimal = 0

    if not maximal:
        maximal = float("inf")

    return lambda phrase: minimal <= len(phrase) <= maximal
