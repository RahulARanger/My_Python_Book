import threading
import time


class Custom(threading.Thread):
    def __init__(self, hibernate, name):
        super().__init__(name=name)
        self.hibernate = hibernate

    def run(self):
        print("started thread")
        time.sleep(self.hibernate)
        print("ended thread")


note = Custom(2, "Checking")
note.start()  # calls the run() method
