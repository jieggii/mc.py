from mc import exceptions
from random import choice

_START = 'NELwi29w{start}NELwi29w'
_END = 'PTqLz8ZS{end}PTqLz8ZS'


class StringGenerator:
    def __init__(self, learning_data: list):
        """
        :param learning_data: list of strings e.g. ['fish 1', 'fish 2', 'fish 3', 'fish red', 'fish big']
        """
        self.learning_data = learning_data

    def generate(self, count: int = 1, min_length: int = 1, lowercase: bool = True):
        """
        :param count: count of generated strings
        :param min_length: minimal length of the string (in words)
        :param lowercase: lowercase all words for better result
        :return: list of generated strings
        """
        if count < 1:
            raise exceptions.InvalidCount('count must be > 0')

        if min_length < 1:
            raise exceptions.InvalidMinimalLength('min_length must be > 0')

        data = []  # ['{start}', 'msg1', '{end}', '{start}', 'msg2', '{end}', ...]
        word_map = {}  # {'word': ['i_can_be_after_"word"', 'i_can_be_after_it_too', ...}
        strings = []  # ['hello world! I am new string', 'I am too!', ...]

        for case in self.learning_data:
            words = case.split(' ')
            data.append(_START)

            for word in words:
                data.append(word.lower()) if lowercase else data.append(word)

            data.append(_END)

        for word in data:
            word_map[word] = []

        for i in range(len(data)):
            if i < len(data) - 1:
                if data[i] != _END:
                    word_map[data[i]].append(data[i+1])

        for i in range(count):
            string = []

            while len(string) < min_length:
                prev_word = _START

                while True:
                    if prev_word:
                        new_word = choice(word_map[prev_word])

                        if new_word == _END:
                            break

                        string.append(new_word)
                        prev_word = new_word

                strings.append(' '.join(string))

        return strings
