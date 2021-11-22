import mc

generator = mc.PhraseGenerator(
    samples=["hello world", "world of cuties"],
    order=2,  # You can set any order for the Markov model (https://en.wikipedia.org/wiki/Variable-order_Markov_model)
)
print(generator.generate_phrase())
# example output: >>> "hello world of cuties"
