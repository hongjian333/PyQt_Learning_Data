from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class ListWidgetDemo(QListWidget):
    def __init__(self):
        super(ListWidgetDemo, self).__init__()
        self.setWindowTitle("QListWidget例子")
        self.resize(300, 270)

        listWidget = QListWidget()
        listWidget.addItem("Item 1")
        listWidget.addItem("Item 2")
        listWidget.addItem("Item 3")
        listWidget.addItem("Item 4")
        listWidget.addItems(["Item 5", 'Item 6'])
        listWidget.itemClicked.connect(self.click)
        listWidget.itemSelectionChanged.connect(self.chagne)

        formLayout = QVBoxLayout()
        formLayout.addWidget(listWidget)
        self.setLayout(formLayout)

    def click(self, qlwt: QListWidgetItem):
        QMessageBox.information(self, "ListWidget", "你选择了:" + qlwt.text())

    def chagne(self):
        QMessageBox.information(self, "ListWidget", "你选择了:")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ListWidgetDemo()
    form.show()
    sys.exit(app.exec_())
