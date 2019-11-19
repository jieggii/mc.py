import mc


generator = mc.StringGenerator(
    samples=["hello world", "world of cuties"]
)  # creating StringGenerator object
result = generator.generate_phrase(
    attempts=25,
    beginning="of",
    validator=mc.util.combine(
        mc.validators.words_count(minimal=2, maximal=2),
        mc.validators.symbols_count(minimal=5, maximal=10),
    ),
    formatter=mc.formatters.usual_syntax,
)  # generating phrase, which starts with "of", has 2 words, from 5 to 10 symbols and formatted like a usual sentence
print(result)
# e.g. >>> "Of cuties."
