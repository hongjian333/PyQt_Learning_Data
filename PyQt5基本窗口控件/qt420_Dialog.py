import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DialogDemo(QWidget):
    def __init__(self):
        super(DialogDemo, self).__init__()
        self.setWindowTitle("Dialog例子")
        self.resize(350, 300)

        self.btn = QPushButton(self)
        self.btn.setText("弹出对话框")
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        btn = QPushButton("OK", dialog)
        btn.move(50, 50)
        dialog.setWindowTitle("Dialog")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DialogDemo()
    form.show()
    sys.exit(app.exec_())
