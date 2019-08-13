import mc


generator = mc.StringGenerator(learning_data=[
    'my name is Egor', 'Egor is programmer'
])

print(generator.generate(count=3))  # e.g. >> ['egor is egor', 'egor is programmer', 'my name is egor']
