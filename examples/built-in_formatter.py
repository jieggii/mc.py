import mc


generator = mc.StringGenerator(
    samples=["hello world", "world of cuties"]
)  # initializing StringGenerator

result = generator.generate_phrase(
    formatter=mc.formatters.usual_syntax  # turns phrase into phrase with usual text syntax
    # e.g. "what a wonderful day! what a nice weather!" -> "What a wonderful day! What a nice weather!"
)  # generating and formatting phrase


print(result)
# e.g. >>> "Hello world of cuties."
