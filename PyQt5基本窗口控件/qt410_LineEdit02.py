from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys


class LineEditDemo(QWidget):
    def __init__(self):
        super(LineEditDemo, self).__init__()
        self.setWindowTitle("QLineEdit例子")

        formLayout = QFormLayout()
        leInt = QLineEdit()
        leDouble = QLineEdit()
        leValidator = QLineEdit()

        formLayout.addRow("整型", leInt)
        formLayout.addRow("浮点型", leDouble)
        formLayout.addRow("字母和数字", leValidator)

        leInt.setPlaceholderText("整型")
        leDouble.setPlaceholderText("浮点型")
        leValidator.setPlaceholderText("字母和数字")

        # 整型，范围：[1,99]
        intValidator = QIntValidator(self)
        intValidator.setRange(1, 99)

        # 浮点型，范围：[-360,360]，精度：小数点后两位
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360, 360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)

        # 字母和数字
        reg = QRegExp("[a-zA-Z0-9]+$")
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        # 设置验证器
        leInt.setValidator(intValidator)
        leDouble.setValidator(doubleValidator)
        leValidator.setValidator(validator)

        self.setLayout(formLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = LineEditDemo()
    form.show()
    sys.exit(app.exec_())
