import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, Qt


class CalendarDemo(QWidget):
    def __init__(self):
        super(CalendarDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.cal = QCalendarWidget(self)
        self.cal.setFirstDayOfWeek(Qt.Sunday)
        self.cal.setMinimumDate(QDate(1980, 1, 1))
        self.cal.setMaximumDate(QDate(3000, 1, 1))
        self.cal.setGridVisible(True)
        self.cal.clicked.connect(self.showDate)
        self.lb = QLabel(self)
        self.lb1 = QLabel(self)
        date: QDate = self.cal.selectedDate()

        self.lb.setText(date.toString("yyyy-MM-dd dddd"))
        self.lb1.setText(str(date.weekNumber()[0]))
        self.lb.move(20, 300)
        self.lb1.move(20, 320)
        self.setGeometry(100, 100, 400, 350)
        self.setWindowTitle("Calendar例子")

    def showDate(self, date: QDate):
        self.lb.setText(date.toString("yyyy-MM-dd dddd"))
        self.lb1.setText(str(date.weekNumber()[0]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = CalendarDemo()
    form.show()
    sys.exit(app.exec_())
