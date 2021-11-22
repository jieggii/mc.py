# Overview

## What is **mc.py**?
**mc.py** is a tiny and trivial Python module which provides you 
a simple way to generate phrases using Markov chains.

## What it can be used for?
I think it is mostly just for fun. I know that some devs 
use this or similar modules for chat-bots to generate funny 
messages (e.g. [VK bot Witless](https://vk.com/witless) or 
[VK bot Sglypa](https://vk.com/sglypa)). I used it to generate
cringy gopnik-style quotes.

## Worth reading before start
_(It is complicated and absolutely optional, but quite interesting)._

* [Markov chain (Wikipedia)](https://en.wikipedia.org/wiki/Markov_chain)
* [Markov model (Wikipedia)](https://en.wikipedia.org/wiki/Markov_model)
* [Variable order Markov model (Wikipedia)](https://en.wikipedia.org/wiki/Variable-order_Markov_model)
* [Создаем генератор текста на основе цепей Маркова: теория и практика (tproger.ru)](https://tproger.ru/translations/markov-chains/)

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
