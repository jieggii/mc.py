import mc


generator = mc.StringGenerator(
    learning_data=[
        'hello world', 'world of cuties', 'hello cuties'
    ],
    order=1
)

print(generator.generate(count=3))  # e.g. >> ['Hello world of cuties', 'Hello world', 'Hello cuties']

