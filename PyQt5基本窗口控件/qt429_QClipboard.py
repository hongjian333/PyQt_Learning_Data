import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QMimeData


class QClipboardDemo(QWidget):
    def __init__(self):
        super(QClipboardDemo, self).__init__()
        textCopyButton = QPushButton("Copy Text")
        textPasteButton = QPushButton("Paste Text")
        htmlCopyButton = QPushButton("Copy HTML")
        htmlPasteButton = QPushButton("Paste HTML")
        imageCopyButton = QPushButton("Copy Image")
        imagePasteButton = QPushButton("Paste Iamge")

        self.textLabel = QLabel("Original Text")
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap("images/close.ico"))

        formLayout = QGridLayout()
        formLayout.addWidget(textCopyButton, 0, 0)
        formLayout.addWidget(imageCopyButton, 0, 1)
        formLayout.addWidget(htmlCopyButton, 0, 2)
        formLayout.addWidget(textPasteButton, 1, 0)
        formLayout.addWidget(imagePasteButton, 1, 1)
        formLayout.addWidget(htmlPasteButton, 1, 2)
        formLayout.addWidget(self.textLabel, 2, 0, 1, 2)
        formLayout.addWidget(self.imageLabel, 2, 2)

        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)

        self.setLayout(formLayout)
        self.setWindowTitle("Clicpboard例子")

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText("I've been clipped!")

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap("images/python.png"))

    def pasteImage(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        print(mimeData)
        if mimeData.hasImage():
            self.imageLabel.setPixmap(mimeData.imageData())
        # self.imageLabel.setPixmap(clipboard.pixmap())

    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml("<b>Bold and <font color=red>Red</font></b>")
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QClipboardDemo()
    form.show()
    sys.exit(app.exec_())
