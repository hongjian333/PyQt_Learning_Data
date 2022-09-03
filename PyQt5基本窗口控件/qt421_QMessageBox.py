import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("QMessageBox例子")
        self.resize(300, 100)
        formLayout = QVBoxLayout()

        # information
        self.btn1 = QPushButton("information")
        self.btn1.clicked.connect(self.onBtn1Clicked)
        formLayout.addWidget(self.btn1)

        # question
        self.btn2 = QPushButton("question")
        self.btn2.clicked.connect(self.onBtn2Clicked)
        formLayout.addWidget(self.btn2)

        # critical
        self.btn3 = QPushButton("critical")
        self.btn3.clicked.connect(self.onBtn3Clicked)
        formLayout.addWidget(self.btn3)

        # critical
        self.btn4 = QPushButton("about")
        self.btn4.clicked.connect(self.onBtn4Clicked)
        formLayout.addWidget(self.btn4)

        self.setLayout(formLayout)

    def onBtn1Clicked(self):
        reply = QMessageBox.information(self, "标题", "消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(reply)

    def onBtn2Clicked(self):
        reply = QMessageBox.question(self, "标题", "消息正文", QMessageBox.Ok | QMessageBox.No, QMessageBox.No)
        print(reply)

    def onBtn3Clicked(self):
        reply = QMessageBox.critical(self, "标题", "消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        print(reply)

    def onBtn4Clicked(self):
        reply = QMessageBox.about(self, "标题", "消息正文")
        print(reply)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
