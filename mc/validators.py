from typing import Optional, Callable

from mc import exceptions as _exceptions


def default(_):
    """
    A stub when there is no validation needed.
    """
    return True


def words_count(
    minimal: Optional[int] = None, maximal: Optional[int] = None
) -> Callable[[str], bool]:
    """
    Returns a function that returns if the amount of words in a given text is
    bigger than minimal and smaller then maximum (not strict)
    :raises ValidationError if both minimal and maximal are None
    :param minimal: Minimal amount of words
    :param maximal: Maximum amount of words
    :return: The comparing function
    """
    if minimal is None and maximal is None:
        raise _exceptions.ValidatorError(
            "minimal and maximal can't be both unspecified"
        )

    if not minimal:
        minimal = 0

    if not maximal:
        maximal = float("inf")

    return lambda phrase: minimal <= len(phrase.split(" ")) <= maximal


def symbols_count(minimal: int = None, maximal: int = None) -> Callable:
    """
    Returns a function that returns if the amount of symbols in a given text is
    bigger than minimal and smaller then maximum (not strict)
    :raises ValidationError if both minimal and maximal are None
    :param minimal: Minimal amount of symbols
    :param maximal: Maximum amount of symbols
    :return: The comparing function
    """
    if minimal is None and maximal is None:
        raise _exceptions.ValidatorError(
            "minimal and maximal can't be both unspecified"
        )

    if not minimal:
        minimal = 0

    if not maximal:
        maximal = float("inf")

    return lambda phrase: minimal <= len(phrase) <= maximal
