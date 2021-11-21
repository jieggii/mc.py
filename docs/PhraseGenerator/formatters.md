# Formatters
Formatters in `mc.py` are functions that format result phrase.
They accept `str` and return `str`.

`mc.py` currently have only one built-in formatter. It is located
at `mc.builtin.formatters`.

## Builtin formatters
`usual_syntax` - formats phrase as usual sentences: 
Uppercase first letter, etc.

Example:
```python
from mc.builtin.formatters import usual_syntax


text = "hello, world! well"
formatted_text = usual_syntax(text)

print(formatted_text)
# >>> "Hello, world! Well."
```

## Writing my own formatter
It's easy! Just keep in mind that formatter should accept `str`, 
do something with it and return formatted `str`.

Example:
```python
from mc import PhraseGenerator


def my_formatter(phrase: str) -> str:
    return "The computer says: " + phrase

generator = PhraseGenerator(samples=[...])
generator.generate_phrase(formatters=[my_formatter])
```