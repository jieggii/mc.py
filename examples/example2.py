import mc


markov = mc.StringGenerator(learning_data=[
    'my name is Egor', 'Egor is programmer'
])

print(markov.generate(count=3, min_length=2))  # e.g. >> ['egor is egor', 'egor is programmer', 'my name is egor']
