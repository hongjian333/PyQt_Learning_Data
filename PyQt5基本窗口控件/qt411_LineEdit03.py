from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
import sys


class LineEditDemo(QWidget):
    def __init__(self):
        super(LineEditDemo, self).__init__()

        self.setWindowTitle("QLineEdit的输入掩码例子")

        formLayout = QFormLayout()
        leIP = QLineEdit()
        leMac = QLineEdit()
        leDate = QLineEdit()
        leLicense = QLineEdit()

        leIP.setInputMask("000.000.000.000;_")
        leMac.setInputMask("HH:HH:HH:HH:HH:HH;_")
        leDate.setInputMask("0000-00-00")
        leLicense.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        formLayout.addRow("数字掩码", leIP)
        formLayout.addRow("Mac掩码", leMac)
        formLayout.addRow("日期掩码", leDate)
        formLayout.addRow("许可证掩码", leLicense)

        self.setLayout(formLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = LineEditDemo()
    form.show()
    sys.exit(app.exec_())
