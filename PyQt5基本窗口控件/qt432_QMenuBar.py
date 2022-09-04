import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MenuDemo(QMainWindow):
    def __init__(self):
        super(MenuDemo, self).__init__()
        formLayout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        save = QAction("Save", self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)
        edit = file.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("Paste")
        quit = QAction(QIcon("images/close.ico"), "Quit", self)
        file.addAction(quit)
        file.triggered.connect(self.processTrigger)
        self.setLayout(formLayout)
        self.setWindowTitle("menu例子")

    def processTrigger(self, q):
        print(q.text() + " is triggered")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MenuDemo()
    form.show()
    sys.exit(app.exec_())
