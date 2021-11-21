# The very beginning

## What is mc.py?
mc.py is a tiny and trivial Python module which provides you 
a simple way to generate phrases using Markov chains.

## Scope of application
I think it is mostly just for fun. I know that some devs 
use this or similar modules for chat-bots to generate funny 
messages (e.g. [VK bot Witless](https://vk.com/witless) or 
[VK bot Sglypa](https://vk.com/sglypa)). I used it to generate
funny cringy gopnik-like quotes.

## Worth reading before start
*(It is complicated and absolutely optional, but quite interesting).*

* [Markov chain (Wikipedia)](https://en.wikipedia.org/wiki/Markov_chain)
* [Markov model (Wikipedia)](https://en.wikipedia.org/wiki/Markov_model)
* [Variable order Markov model (Wikipedia)](https://en.wikipedia.org/wiki/Variable-order_Markov_model)
* [Создаем генератор текста на основе цепей Маркова: теория и практика (tproger.ru)](https://tproger.ru/translations/markov-chains/)

## Simple usage example
*More examples can be found [here](https://github.com/jieggii/mc.py/tree/master/examples).*

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
