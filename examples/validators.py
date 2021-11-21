import mc
from mc.builtin import validators

generator = mc.PhraseGenerator(samples=["hello world", "world of cuties"])

result = generator.generate_phrase(
    attempts=20, validators=[validators.words_count(minimal=4)]
)  # generates string with words count >= 4
print(result)
# >>> "hello world of cuties"


result = generator.generate_phrase(
    attempts=20, validators=[lambda string: len(string.split()) >= 4]
)  # generates string with words count >= 4
print(result)
# >> "hello world of cuties"


result = generator.generate_phrase(
    attempts=20,
    validators=[
        validators.words_count(minimal=4, maximal=10),
        validators.chars_count(minimal=10, maximal=100),
    ],
)  # generates string with words count from 4 to 10 and symbols count from 10 to 100
print(result)
# >>> "hello world of cuties"
