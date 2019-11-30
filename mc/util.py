import json
import random
from typing import Optional, Dict, Callable, AnyStr, List


def get_random_next_frame(available_frames: Dict) -> Optional[str]:
    population = [frame for frame in available_frames.keys()]
    weights = [weight for weight in available_frames.values()]

    if population:
        return random.choices(population=population, weights=weights)[0]

    else:
        return None


def combine_validators(*validators: Callable) -> Callable:
    def combined_validator(phrase: AnyStr) -> bool:
        for validator in validators:
            if not validator(phrase):
                return False

        return True

    return combined_validator


def combine_formatters(*formatters: Callable):
    def combined_formatter(phrase: AnyStr) -> AnyStr:
        for formatter in formatters:
            phrase = formatter(phrase)

        return phrase

    return combined_formatter


def load_json_samples(filename: AnyStr) -> List:
    """
    Loads samples from a json file

    :param filename: File path
    :return: List of samples
    """
    with open(filename, "r", encoding="utf-8") as file:
        samples = json.load(file)

    if isinstance(samples, list):
        return samples

    else:
        raise RuntimeError(f"{filename}'s content must be list-like")


def load_txt_samples(filename: AnyStr, separator: AnyStr) -> List:
    """
    Load samples from a txt file.

    :raises ValueError: if separator is not a single symbol
    :param filename: File path
    :param separator: Sample separator (must be a single symbol)
    :return: List of samples
    """
    if len(separator) != 1:
        raise ValueError("separator must be a symbol")

    samples = []
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        if content[-1] != separator:
            content += separator

    start = 0
    for i in range(len(content)):
        if i != 0:
            if content[i] == separator and content[i - 1] != "\\":
                samples.append(content[start:i].replace(f"\\{separator}", separator))
                start = i + 1

    return samples
