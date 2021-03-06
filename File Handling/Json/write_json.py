import json
import pathlib

bullets = []
for _ in range(1, 8):
    if _ != 4:
        bullets.append(_)

sex_pistols = {
    "Bullets": [f"Number {_}" for _ in sorted(bullets)],
    "missing": 4,
    "user": "mista",
    "once_used_by": {
        "name": "trish",
        "stand": ""
    }
}
print("preview: ")
print("-------")
print(json.dumps(sex_pistols, indent=4))

json.dump(sex_pistols, (pathlib.Path(__file__).parent / "testing.json").open("w"), indent=4)
# dump() accepts any streams
# dumps() just converts the dict to the json format
# Refer this:
# https://stackoverflow.com/questions/36059194/what-is-the-difference-between-json-dump-and-json-dumps-in-python
