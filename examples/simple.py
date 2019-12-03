import mc


generator = mc.StringGenerator(samples=["hello world", "world of cuties"])

result = generator.generate_string()
print(result)
# e.g. >> "hello world of cuties"
