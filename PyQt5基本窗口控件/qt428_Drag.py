import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class DragDemo(QWidget):
    def __init__(self):
        super(DragDemo, self).__init__()
        self.initUI()

    def initUI(self):
        formLayout = QFormLayout()
        formLayout.addRow(QLabel("请把左边的文本拖拽到右边的下拉菜单中"))
        le = QLineEdit()
        le.setDragEnabled(True)
        cb = Combo("Button", self)
        formLayout.addRow(le, cb)
        self.setLayout(formLayout)
        self.setWindowTitle("简单的拖拽例子")


class Combo(QComboBox):
    def __init__(self, title, parent):
        super(QComboBox, self).__init__(parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        print(event)
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        self.addItem(event.mimeData().text())
        print("拖拽完成")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DragDemo()
    form.show()
    sys.exit(app.exec_())
