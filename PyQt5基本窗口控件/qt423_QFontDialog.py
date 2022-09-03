import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QPushButton


class FontDialogDemo(QWidget):
    def __init__(self):
        super(FontDialogDemo, self).__init__()

        formLayout = QVBoxLayout()

        self.btnFont = QPushButton("choose font")
        self.btnFont.clicked.connect(self.onBtnFontClicked)
        formLayout.addWidget(self.btnFont)

        self.lbFont = QLabel("Hello,测试字体例子")
        formLayout.addWidget(self.lbFont)

        self.setLayout(formLayout)
        self.setWindowTitle("Font Dialog例子")

    def onBtnFontClicked(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbFont.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = FontDialogDemo()
    demo.show()
    sys.exit(app.exec_())
