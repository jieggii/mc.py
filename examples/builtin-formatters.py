import mc
from mc.builtin import formatters

generator = mc.PhraseGenerator(samples=["hello world", "world of cuties"])
phrase = generator.generate_phrase(
    formatters=[formatters.usual_syntax]  # formats generated phrase like a usual sentence
)
print(phrase)
# possible output: >>> "Hello world of cuties."
