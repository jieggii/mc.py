from typing import Callable, List, NoReturn, Optional, Union

from mc import const
from mc.types import Validator, Formatter
from mc.markov_chain import MarkovChain


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

    def generate_phrase_or_none(
        self,
        attempts: int = 25,
        validators: Optional[List[Validator]] = None,
        formatters: Optional[List[Formatter]] = None,
    ) -> Optional[str]:
        """
        Same as generate_phrase but returns None instead of raising PhraseGeneratorError
        """
        try:
            return self.generate_phrase(attempts, validators, formatters)
        except PhraseGeneratorError:
            return None

    def generate_phrase(
        self,
        attempts: int = 25,
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
            PhraseGeneratorError if couldn't generate phrase in provided amount of tries
        """
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

            words = words[1:-1]
            phrase = " ".join(words)

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
            f"Could not generate any phrase after {attempts} attempts. Tip:"
            "try to increase `attempts` value, extend model `samples` "
            "and simplify `validators`, if they were provided."
        )
