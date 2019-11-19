import mc


generator = mc.StringGenerator(samples=["hello world", "world of cuties"])
result = generator.generate_phrase(formatter=mc.formatters.usual_syntax)
print(result)
# e.g. >>> "Hello world of cuties."
