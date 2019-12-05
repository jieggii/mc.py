from ast import literal_eval as make_tuple
from typing import Callable, List, Optional

from mc import constants
from mc import core
from mc import formatters
from mc import util
from mc import validators
from mc.core import MarkovModel

__version__ = "3.1.1"
__author__ = "jieggii"


class StringGenerator:
    samples = None
    order = None
    model = None

    def __init__(self, samples: List[str], order: int = 1):
        if not samples:
            raise ValueError("samples can't be an empty list")

        if order < 1:
            raise ValueError("order can't be less than 1")

        self.samples = samples
        self.order = order
        self.model = core.MarkovModel(samples, order)

    def generate_string(
        self,
        attempts: int = 25,
        validator: Callable = None,
        formatter: Callable = None,
    ) -> Optional[str]:
        """
        Generates a random phrase.
        Only returns the phrases, which are validated by the validator.
        Tries for given amount of attempts, before returning None.
        If a phrase is generated, it's formatted by the formatter.

        :param attempts: count of attempts
        :param validator: function which validates generated string
        :param formatter: function which formats generated string
        :return: generated string
       """
        if not validator:
            validator = validators.default

        if not formatter:
            formatter = formatters.default

        for _ in range(attempts):
            current_frame = self.model.get_full_frame(beginning=(constants.START,))

            result = [word for word in current_frame]
            result.append(self.model.get_random_available_word(frame=current_frame))

            while constants.END not in result:
                phrase_len = len(result)
                current_frame = self.model.get_full_frame(
                    beginning=tuple(result[phrase_len - self.order : phrase_len])
                )
                result.append(self.model.get_random_available_word(frame=current_frame))

            result.remove(constants.START)
            result.remove(constants.END)

            result_str = " ".join(result)

            if validator(result_str):
                return formatter(result_str)

        return None

    def save_state(self):
        """
        Saves the state of the String Generator to a dict.
        Fully compatible with encodings like json (no tuples as dict keys).
        """
        new_model = {}
        model = self.model
        for key, value in model.items():
            new_model[repr(key)] = value
        return {
            "samples": self.samples,
            "order": self.order,
            "model": new_model,
        }

    @staticmethod
    def from_state(state):
        """
        Loads the state of the String Generator from a dict.
        """
        new_model = {}
        for key, value in state["model"].items():
            new_model[make_tuple(key)] = value
        sg = StringGenerator(["test"])
        sg.samples = state["samples"]
        sg.order = state["order"]
        model = MarkovModel(["test"], 1)
        model.update(new_model)
        sg.model = model
        return sg
