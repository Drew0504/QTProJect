# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import random
import sys

GROUPS_SELECTOR = [
    "The Light Land",
    "CEO",
    "Yao Jie",
    "Under One",
    "Phoenix Chck",
    "Blow",
    "Mintyouth",
    "Dawn"
]

COLOR_SELECTOR = [
    "# 000000", "#2F0000", "#600030", "#460046", "#28004D",
    "# 272727", "#4D0000", "#820041", "#5E005E", "#3A006F",
    "# 3C3C3C", "#600000", "#9F0050", "#750075", "#4B0091",
    "# 4F4F4F", "#750000", "#BF0060", "#930093", "#5B00AE",
    "# 5B5B5B", "#930000", "#D9006C", "#AE00AE", "#6F00D2",
    "# 6C6C6C", "#AE0000", "#F00078", "#D200D2", "#8600FF",
    "# E0E0E0", "#FF9797", "#FFC1E0", "#FFBFFF", "#DCB5FF",
    "# F0F0F0", "#FFB5B5", "#FFD9EC", "#FFD0FF", "#E6CAFF",
    "# FCFCFC", "#FFD2D2", "#FFECF5", "#FFE6FF", "#F1E1FF",
    "# FFFFFF", "#FFECEC", "#FFF7FB", "#FFF7FF", "#FAF4FF",
    "# 000079", "#000079", "#003E3E", "#006030", "#006000",
    "# 000093", "#003D79", "#005757", "#01814A", "#007500",
    "# 0000C6", "#004B97", "#007979", "#019858", "#009100",
    "# 0000C6", "#005AB5", "#009393", "#01B468", "#00A600",
    "# 0000E3", "#0066CC", "#00AEAE", "#02C874", "#00BB00",
    "# CECEFF", "#ACD6FF", "#CAFFFF", "#C1FFE4", "#BBFFBB",
    "# DDDDFF", "#C4E1FF", "#D9FFFF", "#D7FFEE", "#CEFFCE",
    "# ECECFF", "#D2E9FF", "#ECFFFF", "#E8FFF5", "#DFFFDF",
    "# FBFBFF", "#ECF5FF", "#FDFFFF", "#FBFFFD", "#F0FFF0",
    "# 467500", "#424200", "#5B4B00", "#844200", "#642100",
    "# 548C00", "#5B5B00", "#796400", "#9F5000", "#842B00",
    "# 64A600", "#737300", "#977C00", "#BB5E00", "#A23400",
    "# 73BF00", "#8C8C00", "#AE8F00", "#D26900", "#BB3D00",
    "# 82D900", "#A6A600", "#C6A300", "#EA7500", "#D94600",
    "# 8CEA00", "#C4C400", "#D9B300", "#FF8000", "#F75000",
    "# DEFFAC", "#FFFFB9", "#FFF0AC", "#FFDCB9", "#FFCBB3",
    "# E8FFC4", "#FFFFCE", "#FFF4C1", "#FFE4CA", "#FFDAC8",
    "# EFFFD7", "#FFFFDF", "#FFF8D7", "#FFEEDD", "#FFE6D9",
    "# F5FFE8", "#FFFFF4", "#FFFCEC", "#FFFAF4", "#FFF3EE",
    "# 613030", "#616130", "#336666", "#484891", "#6C3365",
    "# 743A3A", "#707038", "#3D7878", "#5151A2", "#7E3D76",
    "# 804040", "#808040", "#408080", "#5A5AAD", "#8F4586",
    "# 984B4B", "#949449", "#4F9D9D", "#7373B9", "#9F4D95",
]


class SelectGroup(QWidget):
    def __init__(self):
        super(SelectGroup, self).__init__()
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()

        button1 = QPushButton("Select")
        button2 = QPushButton("close")
        layout2 = QHBoxLayout()
        button3 = QPushButton("close")
        button4 = QPushButton("close")

        button1.clicked.connect(self.click)
        button2.clicked.connect(self.close)

        self.textEdit = QTextBrowser()
        layout.addWidget(button1, 0, Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(button2, 0, Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(button3)
        layout.addWidget(button4, 0, Qt.AlignLeft)
        layout.addWidget(self.textEdit)
        self.setLayout(layout)

    def click(self):
        button = self.sender()

        randGroup, randColor = self.getRandomInfo()
        msg = f"Cingratulations!<br>The selected group is :<br><br>"

        htmlMsg = f"<font color='{randColor}' size='5'>{msg}&nbsp;&nbsp;{randGroup}</font>"
        self.textEdit.setHtml(htmlMsg)

    def getRandomInfo(self):
        return random.choice(GROUPS_SELECTOR),random.choice(COLOR_SELECTOR)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = SelectGroup()
    main.setWindowTitle("Groups Selector")
    main.show()
    sys.exit(app.exec_())