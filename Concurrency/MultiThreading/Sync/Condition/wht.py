import threading
import time


class Parsing:
    def __init__(self):
        self.safe = threading.Condition()

    def parse(self):
        with self.safe:
            print("parsing", threading.currentThread())
            time.sleep(3)
            self.safe.notifyAll()

    def ask(self):
        with self.safe:
            print("waiting", threading.currentThread())

            print(self.safe.wait())

            print("done", threading.currentThread())


sample = Parsing()

threading.Thread(None, sample.parse).start()

for _ in range(3):
    threading.Thread(None, sample.ask).start()
