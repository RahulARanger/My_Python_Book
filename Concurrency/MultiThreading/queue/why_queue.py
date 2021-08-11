import queue
from PySide2 import QtWidgets


class Q(queue.Queue, object):  # since queue.Queue is `type` not `object`
    def __init__(self):
        queue.Queue.__init__(self, maxsize=6)
        object.__init__(self)

    def add_work(self):
        try:
            self.put("Random Work", block=False)
            print("assigning work", "total work to do:", self.qsize())
        except queue.Full:
            print("THis is enough for today")

    def do_work(self):
        try:
            print("Doing", self.get(block=False))
            # time.sleep(3) consider this
        except queue.Empty:
            print("No Work")


class Test(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.do_work = QtWidgets.QPushButton(self)
        self.lyf = Q()
        self.do_work.move(10, 10)
        self.do_work.setText("Do Work")
        self.get_work = QtWidgets.QPushButton(self)
        self.get_work.move(90, 10)
        self.get_work.setText("Get Work")

        self.do_work.clicked.connect(self.lyf.do_work)
        self.get_work.clicked.connect(self.lyf.add_work)


check = QtWidgets.QApplication([])
test = Test()
test.show()
check.exec_()
