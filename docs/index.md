# Overview

## What is **mc.py**?
**mc.py** is a tiny and trivial Python package which provides you 
a simple way to generate phrases using Markov chains.

## What it can be used for?
I think it is mostly just for fun. I know that some devs 
use this or similar packages/algorithms for chat-bots to generate funny 
messages (e.g. [VK bot Witless](https://vk.com/witless) or 
[VK bot Sglypa](https://vk.com/sglypa)). I used it to generate
cringy gopnik-style quotes.

## Worth reading before starting
_(It is complicated and absolutely optional, but quite interesting)._

* [Markov chain (Wikipedia)](https://en.wikipedia.org/wiki/Markov_chain)
* [Markov model (Wikipedia)](https://en.wikipedia.org/wiki/Markov_model)
* [From "What is a Markov Model" to "Here is how Markov Models Work"](https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71)
(**mc.py** is in fact based on this article)

## Installation
Just install it using **pip** or with any other package manager you use... 
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
