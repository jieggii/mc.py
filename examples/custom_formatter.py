import mc


def format_phrase(phrase: str) -> str:  # example custom formatter
    """Turns first letter into uppercase and adds a dot to the end"""
    return phrase[0].upper() + phrase[1:] + "."


generator = mc.StringGenerator(
    samples=["hello world", "world of cuties"]
)  # initializing StringGenerator

result = generator.generate_phrase(
    formatter=format_phrase
)  # generating and formatting phrase

print(result)
# e.g. >>> "Hello world of cuties."
