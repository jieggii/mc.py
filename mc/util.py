from typing import Callable, AnyStr, List
import json


def combine_validators(*validators: Callable) -> Callable:
    """
    Combines all validators into one function that checks if
    all validators return True.

    :param validators: A list of validators
    :return: A function that combines all the validators
    """

    def combined_validator(phrase: AnyStr) -> bool:
        for validator in validators:
            if not validator(phrase):
                return False

        return True

    return combined_validator


def combine_formatters(*formatters: Callable):
    """
    Combines all formatters into one function that checks if
    all formatters return True.

    :param formatters: A list of validators
    :return: A function that combines all the formatters
    """

    def combined_formatter(phrase: AnyStr) -> AnyStr:
        for formatter in formatters:
            phrase = formatter(phrase)

        return phrase

    return combined_formatter


def load_json_samples(path: AnyStr) -> List[str]:
    """
    Loads samples from a json file

    :param path: Path to the target file
    :return: List of samples
    """
    with open(path, "r", encoding="utf-8") as file:
        samples = json.load(file)

    if isinstance(samples, list):
        return samples

    else:
        raise RuntimeError(f"File's content must be list-like")


def load_txt_samples(path: AnyStr, separator: AnyStr) -> List[str]:
    """
    Load samples from a txt file.

    :param path: Path to the target file
    :param separator: Sample separator (must be a single symbol)
    :raises ValueError: if separator is not a single symbol
    :return: List of samples
    """
    if len(separator) != 1:
        raise ValueError("separator must be a single symbol")

    samples = []
    with open(path, "r", encoding="utf-8") as file:
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
