import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QSpinBox


class SpinBoxDemo(QWidget):
    def __init__(self):
        super(SpinBoxDemo, self).__init__()

        self.setWindowTitle("SpinBox例子")
        self.resize(300, 100)

        fomrLayout = QVBoxLayout()

        self.lb1 = QLabel("current value:")
        self.lb1.setAlignment(Qt.AlignCenter)
        fomrLayout.addWidget(self.lb1)

        self.sp = QSpinBox()
        fomrLayout.addWidget(self.sp)
        self.sp.valueChanged.connect(self.valueChange)

        self.setLayout(fomrLayout)

    def valueChange(self):
        self.lb1.setText("current value:" + str(self.sp.value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = SpinBoxDemo()
    form.show()
    sys.exit(app.exec_())
