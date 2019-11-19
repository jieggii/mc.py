import mc


def my_validator(phrase):  # checks if phrase has 4 words
    return len(phrase.split()) == 4


generator = mc.StringGenerator(samples=["hello world", "world of cuties"])
result = generator.generate_phrase(attempts=25, validator=my_validator)
print(result)
# e.g. >>> "hello world of cuties"
