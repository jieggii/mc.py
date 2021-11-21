import mc

generator = mc.PhraseGenerator(samples=["hello world", "world of cuties"])

result = generator.generate_phrase()
print(result)
# possible output: >>> "hello world of cuties"
