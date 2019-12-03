# mc.py [![Project on PyPi](https://img.shields.io/pypi/v/mc.py.svg)](https://pypi.org/project/mc.py/) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/cc6260ef77a6489db85f660e9b0d3e27)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jieggii/mc&amp;utm_campaign=Badge_Grade) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
String generator based on Markov process  
  
## Installation  
`pip3 install mc.py --upgrade`  
  
## Simple example  
```python  
import mc  
  
  
generator = mc.StringGenerator(  
  samples=["hello world", "world of cuties"]  
)  
result = generator.generate_string()
print(result)  
# e.g. >>> "hello world of cuties"  
```  
More examples can be found [here](https://github.com/jieggii/mc.py/tree/master/examples)      
## Features  
* Easy to use  
* Result validating (also built-in validators). [Read more](https://jieggii.github.io/mc.py/)
* Result formatting (also built-in formatters). [Read more](https://jieggii.github.io/mc.py/)
