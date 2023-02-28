
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.line = QLineEdit()
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        self.line.setMaxLength(15)

        self.btn_0 = QPushButton("0")
        self.btn_1 = QPushButton("1")
        self.btn_2 = QPushButton("2")
        self.btn_3 = QPushButton("3")
        self.btn_4 = QPushButton("4")
        self.btn_5 = QPushButton("5")
        self.btn_6 = QPushButton("6")
        self.btn_7 = QPushButton("7")
        self.btn_8 = QPushButton("8")
        self.btn_9 = QPushButton("9")
        self.btn_decimal = QPushButton(".")
        self.btn_clear = QPushButton("C")
        self.btn_add = QPushButton("+")
        self.btn_subtract = QPushButton("-")
        self.btn_multiply = QPushButton("*")
        self.btn_divide = QPushButton("/")
        self.btn_equals = QPushButton("=")

        # Создание сетки для размещения кнопок
        grid = QGridLayout()
        grid.addWidget(self.line, 0, 0, 1, 4)
        grid.addWidget(self.btn_1, 1, 0)
        grid.addWidget(self.btn_2, 1, 1)
        grid.addWidget(self.btn_3, 1, 2)
        grid.addWidget(self.btn_add, 1, 3)
        grid.addWidget(self.btn_4, 2, 0)
        grid.addWidget(self.btn_5, 2, 1)
        grid.addWidget(self.btn_6, 2, 2)
        grid.addWidget(self.btn_subtract, 2, 3)
        grid.addWidget(self.btn_7, 3, 0)
        grid.addWidget(self.btn_8, 3, 1)
        grid.addWidget(self.btn_9, 3, 2)
        grid.addWidget(self.btn_multiply, 3, 3)
        grid.addWidget(self.btn_decimal, 4, 0)
        grid.addWidget(self.btn_0, 4, 1)
        grid.addWidget(self.btn_clear, 4, 2)
        grid.addWidget(self.btn_divide, 4, 3)
        grid.addWidget(self.btn_equals, 5, 0, 1, 4)
