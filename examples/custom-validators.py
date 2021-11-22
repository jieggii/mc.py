import mc

generator = mc.PhraseGenerator(
    samples=["hello world", "world of cuties", "cuties are cute", "my commits are messy"]
)


def my_validator(string: str) -> bool:
    if string[0] == "w":
        return True
    else:
        return False


phrase = generator.generate_phrase(validators=[my_validator])
print(phrase)
# example output: >>> "world of cuties are messy"

phrase = generator.generate_phrase(
    validators=[lambda string: len(string.split()) >= 4]
)  # generates phrase with words count >= 4
print(phrase)
# example output: >>> "my commits are cute"
