import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QComboBox


class ComboBoxDemo(QWidget):
    def __init__(self):
        super(ComboBoxDemo, self).__init__()

        self.setWindowTitle("ComboBox例子")
        self.resize(300, 90)
        formLayout = QVBoxLayout()
        self.lb1 = QLabel("")

        self.cb = QComboBox()
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItems(["Java", "C#", "Python"])
        self.cb.currentIndexChanged.connect(lambda: self.selectionChange(self.cb))

        formLayout.addWidget(self.cb)
        formLayout.addWidget(self.lb1)
        self.setLayout(formLayout)

    def selectionChange(self, cb: QComboBox):
        self.lb1.setText(self.cb.currentText())
        print("Items in the list are :")
        for count in range(self.cb.count()):
            print("item" + str(count) + " = " + self.cb.itemText(count))
        print("Current index", cb.currentIndex(), "selected : ", self.cb.currentText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ComboBoxDemo()
    form.show()
    sys.exit(app.exec_())
