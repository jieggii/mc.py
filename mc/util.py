import random
import typing
import json


def get_random_next_frame(available_frames: typing.Dict) -> typing.Optional[str]:
    population = [frame for frame in available_frames.keys()]
    weights = [weight for weight in available_frames.values()]

    if population:
        return random.choices(population=population, weights=weights)[0]

    else:
        return None


def combine(*args: typing.Callable) -> typing.Callable:
    def combined_validator(phrase: typing.AnyStr) -> bool:
        for validator in args:
            if not validator(phrase):
                return False

        return True

    return combined_validator


def load_json_samples(filename: typing.AnyStr) -> typing.List:
    with open(filename, "r", encoding="utf-8") as file:
        samples = json.load(file)

    if isinstance(samples, list):
        return samples

    else:
        raise RuntimeError(f"{filename}'s content must be list-like")


def load_txt_samples(filename: typing.AnyStr, separator: typing.AnyStr) -> typing.List:
    samples = []
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    start = 0
    for i in range(len(content)):
        if i != 0:
            if content[i] == separator and content[i - 1] != "\\":
                samples.append(content[start:i].replace(f"\\{separator}", separator))
                start = i + 1

    return samples
