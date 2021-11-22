from mc import PhraseGenerator


def grumpy_validator(_: str) -> bool:
    print("I don't like this phrase!")
    return False


generator = PhraseGenerator(samples=["lorem ipsum"])
phrase = generator.generate_phrase_or_none(attempts=1, validators=[grumpy_validator])

if phrase is None:
    print("Oh no! Grumpy validator didn't like generated phrase :(")
else:
    print("Wow! It's impossible!")
