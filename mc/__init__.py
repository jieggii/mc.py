from mc import exceptions
from mc import util
from mc import formatters
from mc import validators
import typing


__version__ = "3.0.6"
__author__ = "jieggii"

_start = "__start__"
_end = "__end__"


class StringGenerator:
    samples = None
    frames = None
    model = None

    def __init__(self, samples: typing.List[str]):
        if not samples:
            raise exceptions.EmptySamples("samples can't be an empty list")

        self.samples = samples
        self.frames = []
        self.model = {}

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
        beginning: typing.AnyStr = None,
        validator: typing.Callable = None,
        formatter: typing.Callable = None,
    ) -> typing.Optional[str]:
        if beginning:
            beginning = _start + " " + beginning

        else:
            beginning = _start

        if not validator:
            validator = validators.default

        if not formatter:
            formatter = formatters.default

        beginning_frames = beginning.split(" ")

        for _ in range(attempts):
            result = beginning_frames
            current_frame = result[-1]

            while current_frame != _end:
                available_next_frames = self.model.get(current_frame)
                if (
                    not available_next_frames
                ):  # this happens only when beginning arg is set
                    raise ValueError(
                        f'Not enough samples to use "{" ".join(beginning_frames[1:])}" as beginning argument'
                    )

                next_frame = util.get_random_next_frame(self.model[current_frame])
                if not next_frame:
                    next_frame = _end

                result.append(next_frame)
                current_frame = next_frame

            result.remove(_start)
            result.remove(_end)

            str_result = " ".join(result)

            if validator(str_result):
                return formatter(str_result)

        return None
