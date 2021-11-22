# PhraseGenerator
High-level interface to generate phrases.

## Creation
`PhraseGenerator` instance is created same way as any class instance.
It's constructor method accepts the following arguments:

* `samples` (`List[str]`) - list of sample phrases to be used to generate new ones.
* `order` (`int`, is `1` as default, should be >= 1) - order of Markov model which will be used to generate phrases.

Example:
```python
from mc import PhraseGenerator


generator = PhraseGenerator(
    samples=["i hate cottage cheese", "cottage cheese is awful"],
    order=1,
)
```

## Methods
### `generate_phrase`

Generates random phrase which was validated by provided [validators](validators.md),
formatted using [formatters](formatters.md) in provided number of attempts.

#### Arguments
* `attempts` (`int`, >= 1, is `1` by default) - amount of attempts 
before giving up generating phrase.
* validators (`list` of `Callable`) - list of [functions that validate result phrase](validators.md).
* formatters (`list` of `Callable`) - list of [functions that format result phrase](formatters.md).

#### Raises
* `PhraseGeneratorError` if generator was not able to generate phrase in given amount of tries.