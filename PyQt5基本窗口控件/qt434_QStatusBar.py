import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMenuBar, QMenu, QMainWindow


class StatusBarDemo(QMainWindow):
    def __init__(self):
        super(StatusBarDemo, self).__init__()
        menuBar = self.menuBar()
        file = menuBar.addMenu("File")
        file.addAction("Show")
        file.triggered.connect(self.processTrigger)
        self.setCentralWidget(QTextEdit())
        self.statusBar().showMessage("Ready")
        # self.statusBar = QStatusBar()
        self.setWindowTitle("QStatusBar例子")
        # self.setStatusBar(self.statusBar)

    def processTrigger(self, q: QAction):
        if q.text() == "Show":
            self.statusBar().showMessage(q.text() + " 菜单选项被点击了", 5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = StatusBarDemo()
    form.show()
    sys.exit(app.exec_())
