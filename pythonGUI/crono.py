from PyQt5 import QtCore
import time
import math


class Crono(QtCore.QThread):
    tick = QtCore.pyqtSignal(int, name="changed")  # New style signal

    def __init__(self, maxtime=1, parent=None):
        super(Crono, self).__init__(parent)
        self.maxtime = maxtime

    def setMaxTime(self, time):
        self.maxtime = time

    def run(self):
        for x in range(1, self.maxtime + 1):
            self.tick.emit(x * math.ceil(100 / self.maxtime))
            print(x)
            time.sleep(1)
