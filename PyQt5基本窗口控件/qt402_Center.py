import sys
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow


class WinForm(QMainWindow):
    def __init__(self):
        super(WinForm, self).__init__()
        self.setWindowTitle("主窗口放在屏幕中间例子")
        self.resize(370, 250)
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)  # 窗口移动到屏幕中间


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
