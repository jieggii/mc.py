import mc


generator = mc.StringGenerator(samples=["hello world", "world of cuties"])
result = generator.generate_phrase(
    attempts=25,
    validator=mc.util.combine_validators(
        mc.validators.symbols_count(minimal=10, maximal=21),
        mc.validators.words_count(minimal=4, maximal=4),
    ),
    formatter=mc.util.combine_formatters(
        lambda phrase: phrase.replace("o", "0"), mc.formatters.uppercase
    ),
)
print(result)
# e.g. >>> "HELL0 W0RLD 0F CUTIES"
