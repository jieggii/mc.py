# mc.py [![Codacy Badge](https://api.codacy.com/project/badge/Grade/cc6260ef77a6489db85f660e9b0d3e27)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jieggii/mc&amp;utm_campaign=Badge_Grade)

My implementation of Markov Chains
## Installation
```
pip install mc.py
```

## Examples

```python
import mc  
  
  
markov = mc.StringGenerator(learning_data=[  
    'hello world', 'world of cuties', 'hello cuties'  
])  
  
print(markov.generate(count=3))  # e.g. >> ['world', 'hello world', 'hello world of cuties']
```