import mc


generator = mc.StringGenerator(learning_data=[
    'hello world', 'world of cuties', 'hello cuties'
])

print(generator.generate(count=3))  # e.g. >> ['world', 'hello world', 'hello world of cuties']
