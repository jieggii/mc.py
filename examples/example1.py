import mc


markov = mc.StringGenerator(learning_data=[
    'hello world', 'world of cuties', 'hello cuties'
])

print(markov.generate(count=3))  # e.g. >> ['world', 'hello world', 'hello world of cuties']
