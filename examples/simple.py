import mc

generator = mc.PhraseGenerator(samples=["hello world", "world of cuties"])
phrase = generator.generate_phrase()
print(phrase)
# example output: >>> "hello world of cuties"
