# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import random
import sys

from QT.conf.config import *


class SelectGroup(QWidget):
    def __init__(self):
        super(SelectGroup, self).__init__()
        self.resize(500, 240)
        self.initUI()

    def initUI(self):
        wwg = QWidget(self)
        w1 = QHBoxLayout(wwg)
        hlayout = QHBoxLayout()
        gridLayout = QGridLayout()

        buttonNames = ['class 3 Group', 'Class 3 Student',
                       'class 4 Group', 'Class 4 Student',
                       '', 'close']
        positions = [(i, j) for i in range(3) for j in range(2)]
        for position, name in zip(positions, buttonNames):
            if name == '':
                continue

            button = QPushButton(name)
            if name == "close":
                button.clicked.connect(self.close)
            if name == "class 3 Group":
                button.clicked.connect(self.getClass3Group)
            if name == "Class 3 Student":
                button.clicked.connect(self.getClass3Student)
            if name == "class 4 Group":
                button.clicked.connect(self.getClass4Group)
            if name == "Class 4 Student":
                button.clicked.connect(self.getClass4Student)

            gridLayout.addWidget(button, *position)
        self.textEdit = QTextBrowser()
        hlayout.addWidget(self.textEdit)
        # gridLayout.addWidget()
        self.move(300, 150)
        w1.addLayout(gridLayout)
        w1.addLayout(hlayout)
        self.setLayout(gridLayout)

    def click(self):
        randGroup, randColor = self.getRandomInfo()
        button = self.sender()

        msg = f"Cingratulations!<br>The selected group is :<br><br>"

        htmlMsg = f"<font color='{randColor}' size='5'>{msg}&nbsp;&nbsp;&nbsp;{randGroup}</font>"
        self.textEdit.setHtml(htmlMsg)

    def getClass3Group(self):
        randGroup, randColor = random.choice(CLASS_3_GROUPS_SELECTOR), random.choice(COLOR_SELECTOR)
        msg = f"Cingratulations!<br>The lucky group is :<br><br>"
        htmlMsg = f"<font color='{randColor}' size='5'>{msg}&nbsp;&nbsp;{randGroup}</font>"
        self.textEdit.setHtml(htmlMsg)

    def getClass4Group(self):
        randGroup, randColor = random.choice(CLASS_4_GROUPS_SELECTOR), random.choice(COLOR_SELECTOR)
        msg = f"Cingratulations!<br>The lucky group is :<br><br>"
        htmlMsg = f"<font color='{randColor}' size='5'>{msg}&nbsp;&nbsp;{randGroup}</font>"
        self.textEdit.setHtml(htmlMsg)

    def getClass3Student(self):
        randStudent, randColor = random.choice(CLASS_3_STUDENTS), random.choice(COLOR_SELECTOR)
        msg = f"Cingratulations!<br>The lucky student is :<br><br>"
        htmlMsg = f"<font color='{randColor}' size='5'>{msg}&nbsp;&nbsp;{randStudent}</font>"
        self.textEdit.setHtml(htmlMsg)

    def getClass4Student(self):
        randStudent, randColor = random.choice(CLASS_4_STUDENTS), random.choice(COLOR_SELECTOR)
        msg = f"Cingratulations!<br>The lucky student is :<br><br>"
        htmlMsg = f"<font color='{randColor}' size='5'>{msg}&nbsp;&nbsp;{randStudent}</font>"
        self.textEdit.setHtml(htmlMsg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = SelectGroup()
    main.setWindowTitle("Groups Selector")
    main.show()
    sys.exit(app.exec_())
