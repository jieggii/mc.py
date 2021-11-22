import random
from typing import List, Optional, Tuple

from mc import const


class MarkovChain(dict):
    def __init__(self, samples: List[str], order: int):
        super(MarkovChain, self).__init__()

        for sample in samples:
            words = [const.START] + sample.lower().split() + [const.END]

            for j in range(len(words) - order):
                current_frame = tuple(words[j : j + order])
                next_word = words[j + order]

                if current_frame not in self:
                    self[current_frame] = {}

                if next_word in self[current_frame]:
                    self[current_frame][next_word] += 1

                else:
                    self[current_frame][next_word] = 1

    def get_available_words(self, frame: Tuple[str, ...]) -> Optional[dict]:
        """Returns available words with weights for `frame`"""
        try:
            return self[frame]
        except KeyError:
            raise ValueError(f"Frame {frame} doesn't exist in the model.")

    def get_random_available_word(self, frame: Tuple[str, ...]) -> Optional[str]:
        """Returns random available word for `frame`"""
        try:
            return random.choices(
                population=list(self[frame].keys()), weights=list(self[frame].values())
            )[0]
        except KeyError:
            raise ValueError(f"Frame {frame} does not exist in the model.")

    def get_full_frame(self, beginning: Tuple[str, ...]) -> Optional[tuple]:
        """Finds frame by it's beginning"""
        possible = []

        for frame in self.keys():
            if frame[0 : len(beginning)] == beginning:
                possible.append(frame)

        try:
            return random.choice(possible)
        except IndexError:
            raise RuntimeError("Too high `order` for these `samples`. Try to reduce it.")
