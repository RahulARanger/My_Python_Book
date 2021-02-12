import pathlib


# Refer this for more: https://docs.python.org/3/library/pathlib.html

def listdir(path):
    store = pathlib.Path(path)
    if not (store.exists() and store.is_dir()):
        # for checking its existence and checking whether its a directory or not
        return False
    collect = store.iterdir()
    return list(collect)


def read_a_file(path):
    store = pathlib.Path(path)
    if store.is_file():
        with store.open(mode="r") as pointer:
            for line in pointer.readlines():
                print(line, end='')


def combine_this(*path):
    store = pathlib.PurePath(*path)
    return str(store)


def split(path):
    store = pathlib.PurePath(path)
    return store.parts


def resolve_dots(path):
    store = pathlib.Path(path)
    return store.resolve(strict=False)
    # raise error when store.exists is False and strict=True


def get_drive(path):
    return pathlib.Path(path).drive


def check_absolute(path):
    return pathlib.Path(path).is_absolute()


def name_ext(path):
    store = pathlib.PurePath(path)
    print("FileName: {}".format(store.name))
    print("Name: '{}' and its extension: '{}'".format(store.stem, store.suffix))


def parents(path):
    return list(pathlib.Path(path).parents)


def where_am_i():
    print("Current Location: {}".format(pathlib.Path.cwd()))
    print("Home Directory: {}".format(pathlib.Path.home()))


def abouts(path):
    # Refer this for more info regarding the parameters: https://docs.python.org/3/library/os.html#os.stat
    print(pathlib.Path(path).stat())


def change_ext(path, new_ext):
    return str(pathlib.Path(path).with_suffix(new_ext))


def change_full_name(path, name):
    return str(pathlib.Path(path).with_name(name))


def give_absolute(file_path):
    # returns the absolute path
    store = pathlib.Path(file_path)
    if store.exists():
        return str(store.resolve())
    else:
        raise FileNotFoundError


def security_enabled(path):
    store = pathlib.Path(path)
    print(store.exists())
    return store.exists() and store.is_reserved()



print(69 * "-")

print('listing all the files in a current directory')
print(listdir(str(pathlib.Path(__file__).parent)))

print(69 * "-")

print("performing open() for now read operation on a file")
read_a_file(__file__)

print(69 * "-")

print("combining the paths")
print(combine_this("dsapy", "A", "GraphA"))

print(69 * "-")

print("splitting the paths")
print(split(__file__))

print(69 * "-")

print("Resolving dots")
print(resolve_dots(str(pathlib.PurePath(__file__, ".."))))

print(69 * "-")

print("drive from the path")
print(get_drive(__file__))
print(get_drive("dsapy/A/GraphA"))

print(69 * "-")
# Empty

print("Checking for the absolute paths")
print(check_absolute(__file__))
print(check_absolute("dsapy//A//GraphA"))

print(69 * "-")

print("Name and extension")
name_ext(__file__)
name_ext(pathlib.Path(__file__).parent)

print(69 * "-")

where_am_i()

print(69 * "-")

print(abouts(__file__))
print(abouts(pathlib.Path(__file__).parent))

print(69 * "-")

print(parents(__file__))

print(69 * "-")

print(change_ext(__file__, ".txt"))
print(change_full_name(__file__, "changed.js"))

print(69 * "-")

print(give_absolute("all_in_one.py"))

print(69 * "-")

print(security_enabled(__file__))
print(security_enabled(str(pathlib.PurePath("C:", "Program Files"))))
print(security_enabled(str(pathlib.PurePath("D:", "myaa nee.m4a"))))

print(69 * "-")
