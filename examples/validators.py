import mc


generator = mc.StringGenerator(samples=["hello world", "world of cuties"])

result = generator.generate_string(
    attempts=20, validator=mc.validators.words_count(minimal=4)
)  # generates string with words count >= 4
print(result)
# e.g. >> "hello world of cuties"


result = generator.generate_string(
    attempts=20, validator=lambda string: len(string.split()) >= 4
)  # generates string with words count >= 4
print(result)
# e.g. >> "hello world of cuties"


result = generator.generate_string(
    attempts=20,
    validator=mc.util.combine_validators(
        mc.validators.words_count(minimal=4, maximal=10),
        mc.validators.symbols_count(minimal=10, maximal=100),
    ),
)  # generates string with words count from 4 to 10 and symbols count from 10 to 100
print(result)
# e.g. >> "hello world of cuties"
