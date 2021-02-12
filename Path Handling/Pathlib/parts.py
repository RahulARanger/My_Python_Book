import pathlib

temp = pathlib.Path(__file__)
store = pathlib.PurePath(temp)  # used for the splitting the paths

print(store, type(store))
print(store.parts, type(store.parts))  # to split the directories/ file in the path

print(pathlib.PurePath(*"dsapy.DS.Stacks".split(".")))  # pathlib.PurePath("dsapy", "DS", "Stacks") combines them

