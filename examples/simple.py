import mc

generator = mc.PhraseGenerator(samples=["hello world", "world of cuties"])

phrase = generator.generate_phrase()
print(phrase)
# possible output: >>> "hello world of cuties"
