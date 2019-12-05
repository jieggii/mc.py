import json

import mc

with open("generator.json") as file:
    generator = mc.StringGenerator.from_state(json.loads(file.read()))

print(generator.generate_string())