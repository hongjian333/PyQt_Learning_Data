import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class DrawingTextDemo(QWidget):
    def __init__(self):
        super(DrawingTextDemo, self).__init__()

        self.setWindowTitle("在窗口中绘制文字")
        self.resize(300, 200)
        self.text = "欢迎学习PyQt5"

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)

        self.drawText(event, painter)
        painter.end()

    def drawText(self, event, painter: QPainter):
        painter.setPen(QColor(0, 0, 255))
        painter.setFont(QFont("SimSun", 20))
        painter.drawText(0, 0, self.text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DrawingTextDemo()
    form.show()
    sys.exit(app.exec_())
