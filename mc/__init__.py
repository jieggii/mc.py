from mc import exceptions as _exceptions
from random import choice as _choice


__version__ = '2.0.1'
__author__ = 'jieggii'

_START = 'T9XR6z6g{start}T9XR6z6g'
_END = 'M7qUmJVV{end}M7qUmJVV'


def _generated_to_string(generated: list):
    string = ''
    for frame in generated:
        for subframe in frame:
            string += ' ' + subframe

    return string[1:].replace(_START + ' ', '').replace(' ' + _END, '')


def _get_random_start_frame(frames: list):
    candidates = []

    for frame in frames:
        if frame[0][0] == _START:
            candidates.append(frame[0])

    return _choice(candidates)


def _get_frames(case: str, order: int):
    words = case.split()

    frames = []
    frame = []

    if len(words) % order == 0:
        for word in words:
            frame.append(word)

            if len(frame) == order:
                frames.append(frame)
                frame = []

        return frames

    else:
        return None


class StringGenerator:
    def __init__(self, learning_data: list, order: int = 1):
        self.learning_data = learning_data
        self.order = order

        self.frames = []
        self.frame_map = {}

        if not self.learning_data:
            raise _exceptions.EmptyLearningData('learning_data can\'t be empty list')

        if self.order < 1:
            raise _exceptions.InvalidOrder('order can\'t be lower than 1')

        for case in self.learning_data:
            case = _START + ' ' + case.lower() + ' ' + _END
            frames = _get_frames(case, self.order)

            if frames:
                self.frames.append(frames)

        if not self.frames:
            raise _exceptions.TooSmallLearningData('too small learning_data for this order. Try to add more learning data or reduce order')

        for i in range(len(self.frames)):
            for j in range(len(self.frames[i])):
                self.frames[i][j] = tuple(self.frames[i][j])

            self.frames[i] = tuple(self.frames[i])

        for frame in self.frames:
            for subframe in frame:
                self.frame_map[subframe] = []

        for i in range(len(self.frames)):
            for j in range(len(self.frames[i])-1):
                self.frame_map[self.frames[i][j]].append(self.frames[i][j+1])

    def generate(self, count: int, upper_first_letter: bool = True):
        generated_strings = []

        for _ in range(count):
            current_frame = _get_random_start_frame(self.frames)
            generated = [current_frame]

            while _END not in current_frame:
                available = self.frame_map[current_frame]

                if not available:
                    available = [_END]

                generated.append(_choice(available))
                current_frame = generated[-1]

            generated_strings.append(_generated_to_string(generated))

        for i in range(len(generated_strings)):
            if upper_first_letter:
                generated_strings[i] = generated_strings[i][0].upper() + generated_strings[i][1:]

        return generated_strings
