import mc


def my_validator(phrase: str) -> bool:  # example validator function
    """Checks if the phrase consists of more than 1 word"""
    return len(phrase.split(" ")) > 1


def my_formatter(phrase: str) -> str:  # example formatter function
    """Turns the phrase into uppercase and adds "!" in the end of the phrase"""
    return phrase.upper() + "."


generator = mc.StringGenerator(  # initializing StringGenerator
    samples=["hello world", "world of cuties"]
)

my_result = generator.generate_phrase(
    attempts=10,  # trying to generate 10 times, else getting None
    beginning="of",  # beginning of the generated phrase is "of"
    validator=my_validator,  # validator function
    formatter=my_formatter,  # formatter function
)  # generating phrase which starts with "of", consists of more than 1 word and is formatted with my_formatter
print(my_result)
# e.g. >>> "OF CUTIES!"


# mc.py also has built-in formatters and validators
mc_result = generator.generate_phrase(
    attempts=10,
    beginning="of",
    validator=mc.validators.symbols_count(
        minimal=1, maximal=30
    ),  # mc.validators.default validate everything (always returns True)
    formatter=mc.formatters.usual_syntax,  # mc.formatters.usual_syntax turn phrase into normal text
    # (e.g. "what a wonderful day! what a nice weather!" -> "What a wonderful day! What a nice weather!"")
)
print(mc_result)
# e.g. >>> "Of cuties."

# you can also combine two or more validators
combined_validators_result = generator.generate_phrase(
    attempts=10,
    validator=mc.validators.combine(
        mc.validators.words_count(minimal=4, maximal=4),
        mc.validators.symbols_count(minimal=21, maximal=21),
    ),
)
print(combined_validators_result)
# e.g. >>> "hello world of cuties"
