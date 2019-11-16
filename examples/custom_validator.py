import mc


def check_phrase(phrase: str) -> bool:  # example custom validator
    """Checks if result has more than 3 words"""
    words_count = len(phrase.split(" "))

    if words_count > 3:
        return True

    else:
        return False


generator = mc.StringGenerator(
    samples=["hello world", "world of cuties"]
)  # initializing StringGenerator

result = generator.generate_phrase(
    attempts=25, validator=check_phrase
)  # generating phrase which consists of more than 3 words

print(result)
# e.g. >>> "hello world of cuties"
