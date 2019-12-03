import mc


samples_from_txt = mc.util.load_txt_samples("samples.txt", separator=";")
print(samples_from_txt)
# >> "['hello world', 'hello world of cutes', 'string with escaped ";"']"

samples_from_json = mc.util.load_json_samples("samples.json")
print(samples_from_json)
# >> ['hello world', 'hello world of cuties']
