from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import Qt
import sys


class LineEditDemo(QWidget):
    def __init__(self):
        super(LineEditDemo, self).__init__()
        # 1 显示文本使用自定义字体、右对齐、只允许输入整数
        le1 = QLineEdit()
        le1.setValidator(QIntValidator())
        le1.setMaxLength(4)
        le1.setAlignment(Qt.AlignRight)
        le1.setFont(QFont("Arial", 20))
        # 2 限制输入小数点后两位
        le2 = QLineEdit()
        le2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        formLayout = QFormLayout()
        formLayout.addRow("integer validator", le1)
        formLayout.addRow("double validator", le2)
        # 3 需要一个输入掩码应用于电话号码
        le3 = QLineEdit()
        le3.setInputMask("+99_9999_999999")
        formLayout.addRow("input mask", le3)
        # 4 需要发射信号textChanged，连接到槽函数textChanged()
        le4 = QLineEdit()
        le4.textChanged.connect(lambda: self.textChanged(le4.text()))
        formLayout.addRow("text change", le4)
        # 5 设置显示模式EchoMode为Password，需要发射editingFinished信号连接到槽函数enterPress()，一旦用户按下了回车键，执行该函数
        le5 = QLineEdit()
        le5.setEchoMode(QLineEdit.Password)
        le5.editingFinished.connect(self.enterPress)
        formLayout.addRow("password", le5)
        # 6 显示一个默认的文本，不能编辑，设置为只读的
        le6 = QLineEdit("hello PyQt5")
        le6.setReadOnly(True)
        formLayout.addRow("read only", le6)

        self.setLayout(formLayout)
        self.setWindowTitle("QLineEdit例子")

    def textChanged(self, text):
        print("输入的内容为：" + text)

    def enterPress(self):
        print("已输入值")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = LineEditDemo()
    form.show()
    sys.exit(app.exec_())
