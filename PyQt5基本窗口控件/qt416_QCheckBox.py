import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QCheckBox


class CheckBoxDemo(QWidget):
    def __init__(self):
        super(CheckBoxDemo, self).__init__()

        groupBox = QGroupBox("checkBoxes")
        groupBox.setFlat(True)

        formLayout = QHBoxLayout()

        self.checkBox1 = QCheckBox("&CheckBox1")
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(self.btnState)
        formLayout.addWidget(self.checkBox1)

        self.checkBox2 = QCheckBox("CheckBox2")
        self.checkBox2.toggled.connect(self.btnState)
        formLayout.addWidget(self.checkBox2)

        self.checkBox3 = QCheckBox("CheckBox3")
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        self.checkBox3.stateChanged.connect(self.btnState)
        formLayout.addWidget(self.checkBox3)

        groupBox.setLayout(formLayout)
        miaiLayout = QVBoxLayout()
        miaiLayout.addWidget(groupBox)

        self.setLayout(miaiLayout)
        self.setWindowTitle("CheckBox Demo")

    def btnState(self):
        chk1Status = self.checkBox1.text() + ", isChecked=" + str(self.checkBox1.isChecked()) + ", checkState=" + str(
            self.checkBox1.checkState()) + "\n"
        chk2Status = self.checkBox2.text() + ", isChecked=" + str(self.checkBox2.isChecked()) + ", checkState=" + str(
            self.checkBox2.checkState()) + "\n"
        chk3Status = self.checkBox3.text() + ", isChecked=" + str(self.checkBox3.isChecked()) + ", checkState=" + str(
            self.checkBox3.checkState()) + "\n"
        print(chk1Status, chk2Status, chk3Status)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = CheckBoxDemo()
    form.show()
    sys.exit(app.exec_())
