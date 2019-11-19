import mc


generator = mc.StringGenerator(samples=["hello world", "world of cuties"])
result = generator.generate_phrase(
    beginning="of"
)  # generating phrase witch begins with "of"
print(result)
# e.g. >>> "of cuties"
