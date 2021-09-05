import threading
import time


class Parser:
    def __init__(self):
        self.ev = threading.Event()
        self.raw = 0

    def parse(self):
        time.sleep(3)
        self.raw = 69
        self.ev.set()

    def result(self):
        print(self.raw)

        print(self.ev.wait())

        print(self.raw)


sample = Parser()

for _ in range(1):
    threading.Thread(None, sample.result).start()

threading.Thread(None, sample.parse).start()

