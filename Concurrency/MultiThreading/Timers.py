import threading


def speak(*args, fav=66):
    print("Now Speak", *args, fav)


sample = threading.Timer(2.3, speak, ("Hello", "There"), {"fav": 69})
sample = sample  # a thread object

sample.start()
