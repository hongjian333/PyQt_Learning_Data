import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class DrawingBrush(QWidget):
    def __init__(self):
        super(DrawingBrush, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 365, 280)
        self.setWindowTitle("画刷例子")

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawLines(painter)
        painter.end()

    def drawLines(self, painter: QPainter):
        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 15, 90, 60)

        brush = QBrush(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 15, 90, 60)

        brush = QBrush(Qt.Dense2Pattern)
        painter.setBrush(brush)
        painter.drawRect(250, 15, 90, 60)

        brush = QBrush(Qt.Dense3Pattern)
        painter.setBrush(brush)
        painter.drawRect(10, 105, 90, 60)

        brush = QBrush(Qt.DiagCrossPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 105, 90, 60)

        brush = QBrush(Qt.Dense5Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 105, 90, 60)

        brush = QBrush(Qt.Dense6Pattern)
        painter.setBrush(brush)
        painter.drawRect(250, 105, 90, 60)

        brush = QBrush(Qt.HorPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 195, 90, 60)

        brush = QBrush(Qt.VerPattern)
        painter.setBrush(brush)
        painter.drawRect(130, 195, 90, 60)

        brush = QBrush(Qt.BDiagPattern)
        painter.setBrush(brush)
        painter.drawRect(250, 195, 90, 60)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DrawingBrush()
    form.show()
    sys.exit(app.exec_())
