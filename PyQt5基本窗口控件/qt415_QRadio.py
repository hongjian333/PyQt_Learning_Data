import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QRadioButton


class RadioDemo(QWidget):
    def __init__(self):
        super(RadioDemo, self).__init__()
        formLayout = QHBoxLayout()

        self.btn1 = QRadioButton("button1")
        self.btn1.setChecked(True)
        self.btn1.toggled.connect(lambda: self.btnState(self.btn1))
        formLayout.addWidget(self.btn1)

        self.btn2 = QRadioButton("button2")
        self.btn2.toggled.connect(lambda: self.btnState(self.btn2))
        formLayout.addWidget(self.btn2)

        self.setLayout(formLayout)
        self.setWindowTitle("RaidoButton例子")

    def btnState(self, btn: QRadioButton):
        if btn.text() == "button1":
            if btn.isChecked():
                print(btn.text() + " is selected")
            else:
                print(btn.text() + " is deselected")

        if btn.text() == "button2":
            if btn.isChecked():
                print(btn.text() + " is selected")
            else:
                print(btn.text() + " is deselected")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = RadioDemo()
    form.show()
    sys.exit(app.exec_())
