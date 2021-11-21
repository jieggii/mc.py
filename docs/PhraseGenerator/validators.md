# Validators
Validators in `mc.py` are functions that validate result phrase.
They accept `str` and return `bool` (`True` or `False`) according to
whether they "liked" the phrase.

`mc.py` currently have two built-in validators. They are located
at `mc.builtin.validators`.

## Builtin validators
* `words_count` - validates phrase by words count.
* `chars_count` - validates phrase by symbols count.

Example:
```python
from mc import PhraseGenerator
from mc.builtin import validators


generator = PhraseGenerator(samples=[...])
generator.generate_phrase(
    validators=[
        validators.words_count(minimal=2, maximal=5),
        validators.chars_count(minimal=6, maximal=99)
    ]
)
```

## Writing my own validator
It's simple! Just keep in mind that validator should accept `str`, 
do some checks and return `True` or `False`.

Example:
```python
from mc import PhraseGenerator


def my_validator(phrase: str) -> bool:
    if phrase.startswith("jija"):
        return True
    else:
        return False 

generator = PhraseGenerator(samples=[...])
generator.generate_phrase(validators=[my_validator])
```