import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class DrawingPointDemo(QWidget):
    def __init__(self):
        super(DrawingPointDemo, self).__init__()

        self.resize(300, 200)
        self.setWindowTitle("在窗口中绘制点")

    def paintEvent(self, event):
        # 初始化绘制工具
        painter = QPainter()
        # 开始绘制
        painter.begin(self)
        # 自定义绘制方法
        self.drawPoints(painter)
        # 结束绘制
        painter.end()

    def drawPoints(self, painter: QPainter):
        painter.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            # 绘制正弦函数图形，它的周期是【-200，200】
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0
            painter.drawPoint(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DrawingPointDemo()
    form.show()
    sys.exit(app.exec_())
