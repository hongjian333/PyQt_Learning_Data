import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QCoreApplication


class QLbaelDemo(QDialog):
    def __init__(self):
        super(QLbaelDemo, self).__init__()

        self.setWindowTitle("QLabel例子")
        lbName1 = QLabel("&Name", self)
        leName1 = QLineEdit(self)
        lbName1.setBuddy(leName1)

        lbName2 = QLabel("&Password", self)
        leName2 = QLineEdit(self)
        lbName2.setBuddy(leName2)

        btnOk = QPushButton("&OK", self)
        btnCancel = QPushButton("&Cancel")
        btnOk.clicked.connect(lambda: self.onBtnClicked(leName1.text()))
        btnCancel.clicked.connect(lambda: self.onBtnClicked(leName2.text()))

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(lbName1, 0, 0)
        mainLayout.addWidget(leName1, 0, 1, 1, 2)
        mainLayout.addWidget(lbName2, 1, 0)
        mainLayout.addWidget(leName2, 1, 1, 1, 2)
        mainLayout.addWidget(btnOk, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)

    def onBtnClicked(self, text):
        QMessageBox.information(self, "提示", text, QMessageBox.StandardButton.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QLbaelDemo()
    form.show()
    sys.exit(app.exec_())
