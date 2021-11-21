import mc
from mc.builtin import formatters

generator = mc.PhraseGenerator(samples=["hello world", "world of cuties"])

result = generator.generate_phrase(
    formatters=[formatters.usual_syntax]  # formats result like a usual sentence
)
print(result)
# possible output: >>> "Hello world of cuties."


result = generator.generate_phrase(
    formatters=[
        lambda string: string.replace("o", "0"),
        formatters.usual_syntax
    ]
)  # formats result like a usual sentence and replaces "o" with "0"
print(result)
# possible output: >>> "Hell0 w0rld."
