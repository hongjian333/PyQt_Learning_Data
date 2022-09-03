import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class FileDialogDemo(QWidget):
    def __init__(self):
        super(FileDialogDemo, self).__init__()

        formLayout = QVBoxLayout()

        self.btn = QPushButton("加载图片")
        self.btn.clicked.connect(self.onBtnClicked)
        formLayout.addWidget(self.btn)

        self.lb = QLabel("")
        formLayout.addWidget(self.lb)

        self.btn1 = QPushButton("加载文本文件")
        self.btn1.clicked.connect(self.onBtn1Clicked)
        formLayout.addWidget(self.btn1)

        self.contents = QTextEdit()
        formLayout.addWidget(self.contents)

        self.setLayout(formLayout)
        self.setWindowTitle("File Dialog例子")

    def onBtnClicked(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", r"c:\\", "Image files (*.jpg *.gif)")
        self.lb.setPixmap(QPixmap(fileName))

    def onBtn1Clicked(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Dirs)

        if dlg.exec_():
            fileNames = dlg.selectedFiles()
            f = open(fileNames[0], "r")

            with f:
                data = f.read()
                self.contents.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = FileDialogDemo()
    demo.show()
    sys.exit(app.exec_())
