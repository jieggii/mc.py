import mc


generator = mc.StringGenerator(
    samples=["hello world", "world of cuties"]
)  # initializing StringGenerator

result = generator.generate_phrase(
    attempts=20, validator=mc.validators.words_count(minimal=4, maximal=7)
)  # generating phrase which matches condition 4 <= (count of words in the generated phrase) <= 7
print(result)
# e.g. >>> "hello world of cuties"
