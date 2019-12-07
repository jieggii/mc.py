from typing import Callable, List, Optional, Union

from mc import validators
from mc import formatters
from mc import constants
from mc import core
from mc import util


__version__ = "3.1.1"
__author__ = "jieggii"


def generate_string(
        model: core.MarkovModel = None,
        samples: Optional[List[str]] = None,
        order: int = 1,
        attempts: int = 25,
        validator: Callable = None,
        formatter: Callable = None,
) -> Optional[str]:
    """
    Generates a random phrase.
    Only returns the phrases, which are validated by the validator.
    Tries for given amount of attempts, before returning None.
    If a phrase is generated, it's formatted by the formatter.

    :param model: markov model
    :param samples: samples
    :param order:
    :param attempts: count of attempts
    :param validator: function which validates generated string
    :param formatter: function which formats generated string
    :return: generated string
   """
    if not model:
        if not samples:
            raise ValueError("Samples list can't be empty if model isn't passed")
        model = core.MarkovModel(samples, order)

    if not validator:
        validator = validators.default

    if not formatter:
        formatter = formatters.default

    for _ in range(attempts):
        current_frame = model.get_full_frame(beginning=(constants.START,))

        result = [word for word in current_frame]
        result.append(model.get_random_available_word(frame=current_frame))

        while constants.END not in result:
            phrase_len = len(result)
            current_frame = model.get_full_frame(
                beginning=tuple(result[phrase_len - self.order: phrase_len])
            )
            result.append(model.get_random_available_word(frame=current_frame))

        result.remove(constants.START)
        result.remove(constants.END)

        result_str = " ".join(result)

        if validator(result_str):
            return formatter(result_str)

    return None


class StringGenerator:
    samples: Optional[List[str]]
    order: Optional[int]
    model: Optional[core.MarkovModel]

    def __init__(self, samples: List[str] = None, order: int = 1):
        if order < 1:
            raise ValueError("order can't be less than 1")

        self.samples = samples or list()
        self.order = order
        self.model = core.MarkovModel(samples, order)

    def generate_string(
            self,
            samples: Optional[List[str]] = None,
            order: int = 1,
            attempts: int = 25,
            validator: Callable = None,
            formatter: Callable = None,
    ) -> Optional[str]:
        """
        Generates a random phrase.
        Only returns the phrases, which are validated by the validator.
        Tries for given amount of attempts, before returning None.
        If a phrase is generated, it's formatted by the formatter.

        :param samples: samples
        :param order:
        :param attempts: count of attempts
        :param validator: function which validates generated string
        :param formatter: function which formats generated string
        :return: generated string
       """
        if not samples:
            args = {"model": self.model}
        else:
            args = {}

        return generate_string(samples=samples,
                               order=order,
                               attempts=attempts,
                               formatter=formatter,
                               validator=validator,
                               **args)

