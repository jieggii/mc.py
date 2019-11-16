import mc


def my_validator1(phrase: str) -> bool:  # example validator 1
    return len(phrase) > 20


def my_validator2(phrase: str) -> bool:  # example validator 2
    return len(phrase.split(" ")) > 3


generator = mc.StringGenerator(
    samples=["hello world", "world of cuties"]
)  # initializing StringGenerator

result = generator.generate_phrase(
    attempts=20, validator=mc.validators.combine(my_validator1, my_validator2)
)  # generating phrase which matches both conditions: count of symbols > 20 and count of words > 3

print(result)
# e.g >>> "hello world of cuties"
