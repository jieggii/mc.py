import mc


generator = mc.StringGenerator(
    samples=["hello world", "world of cuties"]
)  # initializing StringGenerator

result = generator.generate_phrase(
    beginning="of"
)  # generating phrase with beginning "of"

print(result)
# e.g >>> "of cuties"
