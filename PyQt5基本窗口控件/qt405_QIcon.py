import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon


class IconForm(QWidget):
    def __init__(self):
        super(IconForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("程序图标")
        self.setGeometry(300, 300, 250, 150)
        self.setWindowIcon(QIcon("images/cartoon1.ico"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = IconForm()
    form.show()
    sys.exit(app.exec_())
