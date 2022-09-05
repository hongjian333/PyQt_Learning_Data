from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class ListViewDemo(QWidget):
    def __init__(self):
        super(ListViewDemo, self).__init__()
        self.setWindowTitle("QListView例子")
        self.resize(300, 270)
        formLayout = QVBoxLayout()

        listView = QListView()
        strListMode = QStringListModel()
        self.qList = ["Item 1", "Item 2", "Item 3", "Item 4"]
        strListMode.setStringList(self.qList)

        listView.setModel(strListMode)
        listView.clicked.connect(self.clicked)

        formLayout.addWidget(listView)
        self.setLayout(formLayout)

    def clicked(self, qModelIndex: QModelIndex):
        QMessageBox.information(self, "ListWidget", "你选择了: " + self.qList[qModelIndex.row()])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ListViewDemo()
    form.show()
    sys.exit(app.exec_())
