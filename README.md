# mc.py
**mc.py** is a tiny and trivial Python package which provides you 
a simple way to generate phrases using Markov chains.

Docs can be found [here](https://jieggii.github.io/mc.py).

## Installation
Just install it using **pip** or any other package manager you use... 
Should I seriously teach you this?

`pip install mc.py`

## Simple usage example
_More examples can be found [here](https://github.com/jieggii/mc.py/tree/master/examples)._

```python
import mc
from mc.builtin import validators


generator = mc.PhraseGenerator(
    samples=["hello world", "world of cuties", "bruh"]
)
phrase = generator.generate_phrase(
    validators=[validators.words_count(minimal=4)]
)

print(phrase)
# >>> "hello world of cuties"
```

## Links
* [Documentation](https://jieggii.github.io/mc.py)
* [Examples](https://github.com/jieggii/mc.py/tree/master/examples)
* [Package at PyPi](https://pypi.org/project/mc.py)