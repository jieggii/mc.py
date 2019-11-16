import mc


generator = mc.StringGenerator(
    samples=["hello world", "world of cuties"]
)  # initializing StringGenerator

result = generator.generate_phrase()  # generating phrase

print(result)
# e.g >>> "hello world of cuties"
