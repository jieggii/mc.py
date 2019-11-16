# todo: add variable-order opportunity (https://en.wikipedia.org/wiki/Variable-order_Markov_model)

from mc import exceptions
from mc import util
from mc import formatters
from mc import validators
import typing


__version__ = "3.0.0"
__author__ = "jieggii"

_start = "__start__"
_end = "__end__"


class StringGenerator:
    frames = []
    model = {}

    def __init__(self, samples: list):
        """
        :param samples - list of example strings
        :raises mc.exceptions.EmptySamples if len(samples) == 0
        """
        if not samples:
            raise exceptions.EmptySamples("samples can't be an empty list")

        self.samples = samples

        for sample in self.samples:
            words = sample.lower().split(" ")
            self.frames.append(_start)

            for word in words:
                self.frames.append(word)

            self.frames.append(_end)

        for i in range(len(self.frames) - 1):
            current_frame = self.frames[i]
            next_frame = self.frames[i + 1]

            if current_frame in self.model.keys():
                if next_frame in self.model[current_frame].keys():
                    self.model[current_frame][next_frame] += 1

                else:
                    self.model[current_frame].update({next_frame: 1})

            else:
                self.model[current_frame] = {next_frame: 1}

    def generate_phrase(
        self,
        attempts: int = 1,
        beginning: str = None,
        validator: typing.Callable = None,
        formatter: typing.Callable = None,
    ) -> typing.Optional[str]:
        """
        generates phrase from samples

        :param attempts: - count of attempts to generate phrase
        :param beginning: - desired beginning of the generated phrase
        :param validator: - validator function (todo: docs)
        :param formatter: - formatter function (todo: docs)
        :return: generated phrase or None
        """
        if beginning:
            beginning = _start + " " + beginning

        else:
            beginning = _start

        if not validator:
            validator = validators.default

        if not formatter:
            formatter = formatters.default

        for _ in range(attempts):
            result = [frame for frame in beginning.split(" ")]
            current_frame = result[-1]

            while current_frame != _end:
                next_frame = util.get_random_next_frame(self.model[current_frame])
                if not next_frame:  # if we couldn't reach the end
                    next_frame = _end

                result.append(next_frame)
                current_frame = next_frame

            result.remove(_start)
            result.remove(_end)

            str_result = " ".join(result)

            if validator(str_result):
                return formatter(str_result)

        return None
