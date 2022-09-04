import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QDateTime, QTime


class DateTimeEditDemo(QWidget):
    def __init__(self):
        super(DateTimeEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QDateTimeEdit例子")
        self.resize(300, 90)

        formLayout = QVBoxLayout()
        self.dateEdit = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.dateEdit.setMinimumDate(QDate.currentDate().addDays(-365))  # 设置最小日期
        self.dateEdit.setMaximumDate(QDate.currentDate().addDays(365))  # 设置最大日期
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.dateChanged.connect(self.onDateChanged)
        self.dateEdit.dateTimeChanged.connect(self.onDateTimeChanged)
        self.dateEdit.timeChanged.connect(self.onTimeChanged)

        self.btn = QPushButton("获得日期和事件")
        self.btn.clicked.connect(self.onBtnClicked)

        formLayout.addWidget(self.dateEdit)
        formLayout.addWidget(self.btn)

        self.setLayout(formLayout)

    def onDateChanged(self, date):
        print(date)

    def onDateTimeChanged(self,dateTime):
        print(dateTime)

    def onTimeChanged(self,time):
        print(time)

    def onBtnClicked(self):
        dateTime=self.dateEdit.dateTime()
        maxDate=self.dateEdit.maximumDate()
        minDate=self.dateEdit.minimumDate()
        maxDateTime=self.dateEdit.maximumDateTime()
        minDateTime=self.dateEdit.minimumDateTime()
        maxTime=self.dateEdit.minimumTime()
        minTime=self.dateEdit.maximumTime()
        print("\n选择日期事件")
        print("dateTime=%s" % str(dateTime))
        print("maxDate%s" % str(maxDate))
        print("minDate%s" % str(minDate))
        print("maxDateTime%s" % str(maxDateTime))
        print("minDateTime%s" % str(minDateTime))
        print("maxTime%s" % str(maxTime))
        print("minTime%s" % str(minTime))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DateTimeEditDemo()
    form.show()
    sys.exit(app.exec_())

