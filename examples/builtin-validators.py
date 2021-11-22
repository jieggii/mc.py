import mc
from mc.builtin import validators

generator = mc.PhraseGenerator(samples=["hello world", "world of cuties"])
phrase = generator.generate_phrase(
    validators=[validators.words_count(minimal=4)]
)  # generates phrase with words count >= 4
print(phrase)
# >>> "hello world of cuties"

phrase = generator.generate_phrase(
    validators=[
        validators.words_count(minimal=4, maximal=10),
        validators.chars_count(minimal=10, maximal=100),
    ],
)  # generates phrase with words count from 4 to 10 and symbols count from 10 to 100
print(phrase)
# >>> "hello world of cuties"
