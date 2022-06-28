# PhraseGenerator
High-level interface to generate phrases.

## Initialization
`PhraseGenerator` instance is initializated the same way as any class instance.
Its constructor method accepts the following arguments:

* `samples` (`List[str]`) - list of sample phrases to be used to generate new ones.
* `order` (`int`, >= 1, default is `1`) - order of Markov model which will be used to generate phrases.

Example:
```python
from mc import PhraseGenerator


generator = PhraseGenerator(
    samples=["i hate cottage cheese", "cottage cheese is awful"],
    order=1,
)
```

## Methods
### **`generate_phrase(...)`**

Generates random phrase which was validated by provided [validators](validators.md),
formatted using [formatters](formatters.md) in provided number of attempts.

Arguments:

* `attempts` (`int`, default is `999`) - amount of attempts before giving up generating phrase.
* validators (`list` of `Callable`) - list of [functions that validate result phrase](validators.md).
* formatters (`list` of `Callable`) - list of [functions that format result phrase](formatters.md).

Raises `PhraseGeneratorError` if generator could not generate phrase in given amount of tries.

### **`generate_phrase_or_none(...)`**
Same as `generate_phrase` but returns `None` instead of raising `PhraseGeneratorError`.

### **`generate_phrases(...)`**
Generates given amount of phrases and returns `list` of them.

Arguments:

* count (`int`) - number of generated phrases
* Other arguments are the same as in `generate_phrase`

Raises `PhraseGeneratorError` if generator could not generate phrase in given amount of tries.
