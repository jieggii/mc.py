import mc


generator = mc.StringGenerator(
    learning_data=[
        'my name is Egor', 'Egor is programmer'
    ],
    order=1
)

print(generator.generate(count=3))  # e.g. >> ['My name is egor', 'Egor is egor', 'Egor is egor']

