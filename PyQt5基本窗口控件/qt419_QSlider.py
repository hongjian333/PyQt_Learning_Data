import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QSlider


class SliderDemo(QWidget):
    def __init__(self):
        super(SliderDemo, self).__init__()

        self.setWindowTitle("QSlider例子")
        self.resize(300, 100)

        formLayout = QVBoxLayout()

        self.lb1 = QLabel("Hello PyQt5")
        self.lb1.setAlignment(Qt.AlignCenter)
        formLayout.addWidget(self.lb1)

        self.sld = QSlider(Qt.Horizontal)  # 水平方向
        self.sld.setMinimum(10)  # 设置最小值
        self.sld.setMaximum(50)  # 设置最大值
        self.sld.setSingleStep(3)  # 设置步长
        self.sld.setValue(20)  # 设置当前值
        self.sld.setTickPosition(QSlider.TicksBelow)  # 设置刻度位置，在下方
        self.sld.setTickInterval(5)  # 设置刻度间隔
        self.sld.valueChanged.connect(self.valueChange)
        formLayout.addWidget(self.sld)

        self.setLayout(formLayout)

    def valueChange(self):
        print("current slider value = %s" % self.sld.value())
        size = self.sld.value()
        self.lb1.setFont(QFont("Arial", size))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = SliderDemo()
    form.show()
    sys.exit(app.exec_())
