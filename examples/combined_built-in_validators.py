import mc


generator = mc.StringGenerator(
    samples=["hello world", "world of cuties"]
)  # initializing StringGenerator

result = generator.generate_phrase(
    attempts=25,
    validator=mc.validators.combine(
        mc.validators.symbols_count(minimal=10, maximal=500),
        mc.validators.words_count(minimal=2, maximal=5),
    ),
)  # generating phrase which matches both conditions:
# (count of symbols belongs to {10, 11, ..., 99, 100}) and (count of words belongs to {2, 3, 4, 5})

print(result)
# e.g >>> "hello world"
