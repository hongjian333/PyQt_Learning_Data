import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class InputDialogDemo(QWidget):
    def __init__(self):
        super(InputDialogDemo, self).__init__()

        fomrLayout = QFormLayout()
        self.btn1 = QPushButton("获得列表里的选项")
        self.btn1.clicked.connect(self.getItem)
        self.le1 = QLineEdit()
        fomrLayout.addRow(self.btn1, self.le1)

        self.btn2 = QPushButton("获得字符串")
        self.btn2.clicked.connect(self.getText)
        self.le2 = QLineEdit()
        fomrLayout.addRow(self.btn2, self.le2)

        self.btn3 = QPushButton("获得整数")
        self.btn3.clicked.connect(self.getInt)
        self.le3 = QLineEdit()
        fomrLayout.addRow(self.btn3, self.le3)

        self.setWindowTitle("Input Dialog例子")
        self.setLayout(fomrLayout)

    def getItem(self):
        items = ("C", "C++", "Java", "Python")
        item, ok = QInputDialog.getItem(self, "select input dialog", "语言列表", items, 0, False)
        if ok and item:
            self.le1.setText(item)

    def getText(self):
        text, ok = QInputDialog.getText(self, "Text Input Dialog", "输入姓名:")
        if ok:
            self.le2.setText(str(text))

    def getInt(self):
        num, ok = QInputDialog.getInt(self, "Integer Input Dialog", "输入整数")
        if ok:
            self.le3.setText(str(num))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = InputDialogDemo()
    form.show()
    sys.exit(app.exec_())
