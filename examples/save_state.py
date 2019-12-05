import json

import mc


generator = mc.StringGenerator(samples=["hello world", "world of cuties"])

with open("generator.json", "w") as file:
    file.write(json.dumps(generator.save_state()))
