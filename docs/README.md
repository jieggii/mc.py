# mc.py documentation

## Structure:
*  `Class StringGenerator` - string generator class.
* * <b>Variables</b>:
* * * `frames` [list of tuple of tuple] - list of frames
* * * `frame_map` [dict] - map of frames
* * <b>Functions</b>:
* * * `def __init__(learning_data: list, order: int = 1)` - constructor
* * * * <b>Arguments</b>: 
* * * * `learning_data` [list of strings] - list of learning data
* * * *  `order` [int from 1 to ∞] - Markov Chain order

* * * * <b>Raises</b>:
* * * * * `mc.exceptions.EmptyLearningData` when length of `learning_data` == 0
* * * * * `mc.exceptions.InvalidOrder` when `order` < 1
* * * * * `mc.exceptions.TooSmallLearningData` when length of `frames` == 0
* * *  `def generate(count: int = 1)`
* * * * <b>Arguments:</b>
* * * * *  `count` - count of generated strings
* * * * <b>Returns:</b>
* * * * * Generated strings [list of str]

## Links
* [Project on PyPi](https://pypi.org/project/mc.py/)
* [Homepage](https://github.com/jieggii/mc.py)
