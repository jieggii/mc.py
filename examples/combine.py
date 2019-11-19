import mc


generator = mc.StringGenerator(samples=["hello world", "world of cuties"])
result = generator.generate_phrase(
    attempts=25,
    validator=mc.util.combine(
        mc.validators.symbols_count(minimal=10, maximal=21),
        mc.validators.words_count(minimal=4, maximal=4),
    ),
)
print(result)
# e.g. >>> "hello world of cuties"
