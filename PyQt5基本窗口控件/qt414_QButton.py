import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QPushButton


class Form(QDialog):
    def __init__(self):
        super(Form, self).__init__()
        formLayout = QVBoxLayout()

        self.btn1 = QPushButton("button1")
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(self.btnState)
        self.btn1.clicked.connect(lambda: self.whichBtn(self.btn1))
        formLayout.addWidget(self.btn1)

        self.btn2 = QPushButton("image")
        self.btn2.setIcon(QIcon(QPixmap("images/python.png")))
        self.btn2.clicked.connect(lambda: self.whichBtn(self.btn2))
        formLayout.addWidget(self.btn2)

        self.btn3 = QPushButton("Disable")
        self.btn3.setEnabled(False)
        formLayout.addWidget(self.btn3)

        self.btn4 = QPushButton("&Download")
        self.btn4.setDefault(True)
        self.btn4.clicked.connect(lambda: self.whichBtn(self.btn4))
        formLayout.addWidget(self.btn4)

        self.setLayout(formLayout)
        self.setWindowTitle("Button Demo")

    def btnState(self):
        if self.btn1.isChecked():
            print("button pressed")
        else:
            print("button released")

    def whichBtn(self, btn: QPushButton):
        print("clicked button is " + btn.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
