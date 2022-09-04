import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ToolBarDemo(QMainWindow):
    def __init__(self):
        super(ToolBarDemo, self).__init__()
        self.setWindowTitle("ToolBar例子")
        self.resize(300, 200)

        formLayout = QVBoxLayout()
        toolBar = self.addToolBar("File")
        new = QAction(QIcon("images/new.png"), "New", self)
        toolBar.addAction(new)
        open = QAction(QIcon("images/open.png"), "Open", self)
        toolBar.addAction(open)
        save = QAction(QIcon("images/save.png"), "Save", self)
        toolBar.addAction(save)
        toolBar.actionTriggered.connect(self.toolBtnPressed)
        self.setLayout(formLayout)

    def toolBtnPressed(self, btn: QAction):
        print("Pressed tool button is", btn.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ToolBarDemo()
    form.show()
    sys.exit(app.exec_())
