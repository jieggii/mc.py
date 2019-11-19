import mc


def my_formatter(phrase):  # turns all letters from phrase into uppercase
    return phrase.upper()


generator = mc.StringGenerator(samples=["hello world", "world of cuties"])
result = generator.generate_phrase(formatter=my_formatter)
print(result)
# e.g. >>> "HELLO WORLD OF CUTIES"
