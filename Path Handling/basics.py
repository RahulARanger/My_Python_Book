import pathlib

# Object Oriented File System paths (platform independent, but the nature of the object depends on the platform)
store = pathlib.Path(__file__).parent

print(store, type(store))  # returns the windows object

# to check whether a file is directory or a file

test_file = store / "testfile.txt"  # we use / to go front

print(test_file.is_file())

test_dir = store.parent / "Pathlib"  # we use .parent to go back

print(test_dir.is_dir())

print(test_dir.exists())  # return True if that path exists else False

print(str(test_dir))  # returns the path in the string format
