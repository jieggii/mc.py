import mc


json_samples = mc.util.load_json_samples("samples.json")
print(json_samples)
# >>> ['hello world', 'world of cuties']

txt_samples = mc.util.load_txt_samples("samples.txt", separator=";")
print(txt_samples)
# >>> ['hello world', 'world of cuties']
