# mc.py [![Codacy Badge](https://api.codacy.com/project/badge/Grade/cc6260ef77a6489db85f660e9b0d3e27)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jieggii/mc&amp;utm_campaign=Badge_Grade)

My implementation of Markov Chains

## Installation
```bash
pip install mc.py
```

## Example

```python
import mc


generator = mc.StringGenerator(
    learning_data=[
        'hello world', 'world of cuties'
    ],
    order=1
)
print(generator.generate(1))  # e.g. >> ['Hello world of cuties']
```

## Links
* [Documentation](https://github.com/jieggii/mc.py/blob/master/docs/README.md)
* [Project on PyPi](https://pypi.org/project/mc.py/)