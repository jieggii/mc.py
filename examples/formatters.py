import mc


generator = mc.StringGenerator(samples=["hello world", "world of cuties"])

result = generator.generate_string(
    formatter=mc.formatters.usual_syntax
)  # formats result like a usual sentence
print(result)
# e.g. >> "Hello world of cuties."


result = generator.generate_string(
    formatter=mc.util.combine_formatters(
        lambda string: string.replace("o", "0"), mc.formatters.usual_syntax
    )
)  # formats result like a usual sentence and replaces "o" with "0"
print(result)
# e.g. >> "Hell0 w0rld."
