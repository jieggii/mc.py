from typing import List, NoReturn, Optional, Union

from mc import const
from mc.markov_chain import MarkovChain
from mc.types import Formatter, Validator


class PhraseGeneratorError(RuntimeError):
    def __init__(self, msg: str):
        self.message = msg
        super(PhraseGeneratorError, self).__init__(msg)


class PhraseGenerator:
    def __init__(self, samples: List[str], order: int = 1):
        if not samples:
            raise ValueError("`samples` can't be empty.")

        if order < 1:
            raise ValueError("`order` can't be less than 1.")

        self.samples = samples
        self.order = order
        self.model = MarkovChain(samples, order)

    def generate_phrases(
        self,
        count: int,
        attempts: int = 999,
        validators: Optional[List[Validator]] = None,
        formatters: Optional[List[Formatter]] = None,
    ) -> Union[List[str], NoReturn]:
        """
        Generates given amount of phrases and returns list of them

        Parameters:
            count - count of phrases to generate
            attempts - amount of attempts
            validators - list of functions which validate result phrase
            formatters - list of functions which format result phrase

        Raises:
            - PhraseGeneratorError if was not able to generate phrase in provided amount of attempts
        """
        if count < 1:
            raise ValueError("`count` can't be less than 1.")

        phrases = []
        for _ in range(count):
            try:
                phrase = self.generate_phrase(attempts, validators, formatters)
                phrases.append(phrase)
            except PhraseGeneratorError:
                raise
        return phrases

    def generate_phrase_or_none(
        self,
        attempts: int = 999,
        validators: Optional[List[Validator]] = None,
        formatters: Optional[List[Formatter]] = None,
    ) -> Optional[str]:
        """Same as generate_phrase but returns None instead of raising PhraseGeneratorError"""
        try:
            return self.generate_phrase(attempts, validators, formatters)
        except PhraseGeneratorError:
            return None

    def generate_phrase(
        self,
        attempts: int = 999,
        validators: Optional[List[Validator]] = None,
        formatters: Optional[List[Formatter]] = None,
    ) -> Union[str, NoReturn]:
        """
        Generate a random phrase which was validated by `validators`
        and formatted using `formatters` in provided number of `attempts`

        Parameters:
            attempts - amount of attempts
            validators - list of functions which validate result phrase
            formatters - list of functions which format result phrase

        Raises:
            - PhraseGeneratorError if was not able to generate phrase in provided amount of attempts
        """
        if attempts < 1:
            raise ValueError("`attempts` can't be less than 1")
        for _ in range(attempts):
            current_frame = self.model.get_full_frame(beginning=(const.START,))

            words = [word for word in current_frame]
            words.append(self.model.get_random_available_word(frame=current_frame))

            while const.END not in words:
                phrase_len = len(words)
                current_frame = self.model.get_full_frame(
                    beginning=tuple(words[phrase_len - self.order : phrase_len])
                )
                words.append(self.model.get_random_available_word(frame=current_frame))

            phrase = " ".join(words[1:-1])

            if validators:
                valid = all(map(lambda validator: validator(phrase), validators))
            else:
                valid = True

            if valid:
                if formatters:
                    for formatter in formatters:
                        phrase = formatter(phrase)
                return phrase

        raise PhraseGeneratorError(
            f"Could not generate any phrase after {attempts} attempts. Tip: "
            "try to increase `attempts` value, extend model `samples` "
            "and simplify `validators`, if they were provided."
        )
