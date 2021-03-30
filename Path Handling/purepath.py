import pathlib

store = pathlib.PurePath(__file__).parent

print(store)

print(store.drive)  # returns the root drive if provided with the absolute path else "/"
print(store.root)

print(pathlib.PurePath(__file__).name)
print(store.name)  # returns the name of the folder or the file
