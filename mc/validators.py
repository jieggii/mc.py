from mc import exceptions as _exceptions
import typing


def default(_):
    return True


def words_count(minimal: int = None, maximal: int = None) -> typing.Callable:
    if minimal is None and maximal is None:
        raise _exceptions.ValidatorError(
            "minimal and maximal can't be both unspecified"
        )

    if not minimal:
        minimal = 0

    if not maximal:
        maximal = float("inf")

    return lambda phrase: minimal <= len(phrase.split(" ")) <= maximal


def symbols_count(minimal: int = None, maximal: int = None) -> typing.Callable:
    if minimal is None and maximal is None:
        raise _exceptions.ValidatorError(
            "minimal and maximal can't be both unspecified"
        )

    if not minimal:
        minimal = 0

    if not maximal:
        maximal = float("inf")

    return lambda phrase: minimal <= len(phrase) <= maximal
