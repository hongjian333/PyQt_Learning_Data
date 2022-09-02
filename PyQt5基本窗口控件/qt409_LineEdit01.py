from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QPushButton, QMessageBox
import sys


class LineEditDemo(QWidget):
    def __init__(self):
        super(LineEditDemo, self).__init__()

        self.setWindowTitle("QLineEdit例子")

        formLayout = QFormLayout()
        leNormal = QLineEdit()
        leNoEcho = QLineEdit()
        lePassword = QLineEdit()
        lePasswordEchoOnLineEdit = QLineEdit()
        btn = QPushButton("显示")

        formLayout.addRow("Normal", leNormal)
        formLayout.addRow("NoEcho", leNoEcho)
        formLayout.addRow("Password", lePassword)
        formLayout.addRow("PasswordEchoOnEdit", lePasswordEchoOnLineEdit)
        formLayout.addRow("显示输入文字", btn)

        leNormal.setPlaceholderText("Normal")
        leNoEcho.setPlaceholderText("NoEcho")
        lePassword.setPlaceholderText("Password")
        lePasswordEchoOnLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        # 设置背景效果
        leNormal.setEchoMode(QLineEdit.Normal)
        leNoEcho.setEchoMode(QLineEdit.NoEcho)
        lePassword.setEchoMode(QLineEdit.Password)
        lePasswordEchoOnLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        btn.clicked.connect(lambda: self.onBtnClicked(leNormal.text(), leNoEcho.text(), lePassword.text(),
                                                      lePasswordEchoOnLineEdit.text()))

        self.setLayout(formLayout)

    def onBtnClicked(self, text1, text2, text3, text4):
        QMessageBox.information(self, "输入的文本", text1 + "\r\n" + text2 + "\r\n" + text3 + "\r\n" + text4,
                                QMessageBox.StandardButton.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = LineEditDemo()
    form.show()
    sys.exit(app.exec_())
