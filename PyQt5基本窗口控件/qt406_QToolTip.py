import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QApplication, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont


class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("Microsoft Yahei", 10))
        self.setToolTip("这是一个<b>气泡提示<b>")
        self.setWindowTitle("气泡提示Demo")
        self.resize(300,300)
        btn = QPushButton("Button")
        btn.setToolTip("这是一个按钮")

        formlayout = QHBoxLayout()
        formlayout.addWidget(btn)
        self.setLayout(formlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
