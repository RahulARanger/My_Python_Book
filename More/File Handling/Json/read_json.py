import pathlib
import json

sample_ = (pathlib.Path(__file__).parent / "testing.json")
sample = sample_.read_text()

print("preview in file: ")
print(type(sample))  # string
print(sample)

print("after parsing json format (json.loads())")
print(json.loads(sample))  # 1

print("loading from streams:")
testing = json.load(sample_.open())  # 2
print(testing)

# 1 and # 2 have the same types of dict
