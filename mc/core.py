import random
from typing import List, Tuple, Optional

from mc import constants


class MarkovModel(dict):
    def __init__(self, samples: List[str], order: int):
        super(MarkovModel, self).__init__()

        for sample in samples:
            words = [constants.START] + sample.lower().split(" ") + [constants.END]

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
        """
        Returns available words with weights for specified frame

        :param frame: Target frame
        :return: Available words with weights
        """
        try:
            return self[frame]

        except KeyError:
            raise ValueError(f"Frame {frame} does not exist in the model")

    def get_random_available_word(self, frame: Tuple[str, ...]) -> Optional[str]:
        """
        Returns random available word for specified frame

        :param frame: Target frame
        :return: Random available word for specified frame
        """
        try:
            return random.choices(
                population=list(self[frame].keys()), weights=list(self[frame].values())
            )[0]

        except KeyError:
            raise ValueError(f"Frame {frame} does not exist in the model")

    def get_full_frame(self, beginning: Tuple[str, ...]) -> Optional[tuple]:
        """
        Finds frame by it's beginning

        :param beginning: Beginning of the target frame
        :raises RuntimeError: If can't find full frame
        :return: Full frame
        """
        possible = []

        for frame in self.keys():
            if frame[0 : len(beginning)] == beginning:
                possible.append(frame)

        try:
            return random.choice(possible)

        except IndexError:
            raise RuntimeError("Too big order for these samples. Try to reduce it")
