from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys


class TextEidtDemo(QWidget):
    def __init__(self):
        super(TextEidtDemo, self).__init__()

        self.setWindowTitle("QTextEdit例子")
        self.resize(300, 700)
        self._textEdit = QTextEdit()
        btn1 = QPushButton("显示文本")
        btn2 = QPushButton("显示Html")
        formLayout = QVBoxLayout()
        formLayout.addWidget(self._textEdit)
        formLayout.addWidget(btn1)
        formLayout.addWidget(btn2)
        self.setLayout(formLayout)
        btn1.clicked.connect(self._btn1_Clicked)
        btn2.clicked.connect(self._btn2_Clicked)

    def _btn1_Clicked(self):
        self._textEdit.setPlainText("Hello PyQt5!\n单击按钮")

    def _btn2_Clicked(self):
        self._textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\n单击按钮</font>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = TextEidtDemo()
    form.show()
    sys.exit(app.exec_())
