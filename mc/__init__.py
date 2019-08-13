from mc import exceptions as _exceptions
from random import choice as _choice


_START = '{start}'
_END = '{end}'


class StringGenerator:
    def __init__(self, learning_data: list):
        self.learning_data = learning_data

        self.frames = []
        self.frame_map = {}

        if not self.learning_data:
            raise _exceptions.EmptyLearningData('learning_data can\'t be empty list')

        for case in self.learning_data:
            self.frames.append(_START)

            for word in case.split(' '):
                self.frames.append(word)

            self.frames.append(_END)

        for frame in self.frames:
            self.frame_map[frame] = []

        for i in range(len(self.frames) - 1):
            current_frame = self.frames[i]
            next_frame = self.frames[i+1]

            if current_frame != _END:
                self.frame_map[current_frame].append(next_frame)

    def generate(self, count: int):
        generated_strings = []

        for _ in range(count):
            string = [_START]

            current_frame = _START

            while current_frame != _END:
                available = self.frame_map[current_frame]

                if not available:
                    available = [_END]

                string.append(_choice(available))
                current_frame = string[-1]

            string = ' '.join(string).replace(_START + ' ', '').replace(' ' + _END, '')
            generated_strings.append(string)

        return generated_strings
