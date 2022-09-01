import sys
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QApplication, QWidget


class WinForm(QMainWindow):
    def __init__(self):
        super(WinForm, self).__init__()
        self.setWindowTitle("关闭主窗口例子")
        self.button1 = QPushButton("关闭主窗口")
        self.button1.clicked.connect(self.onButtonClick)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self):  # 关闭主窗口
        sender = self.sender()  # 发送信号的对象
        print(sender.text() + "被按下了")
        qapp = QApplication.instance()
        qapp.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
