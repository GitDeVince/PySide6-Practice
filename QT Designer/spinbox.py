from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from ui_spinbox2 import Ui_Widget

import resource_rc # manually import the compiled resource file

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User Data")
        self.spinbox.setValue(0)
        self.plusbutton.clicked.connect(self.plus)
        self.minusbutton.clicked.connect(self.minus)

    def plus(self):
        value = self.spinbox.value()
        self.spinbox.setValue(value + 1)

    def minus(self):
        value = self.spinbox.value()
        self.spinbox.setValue(value - 1)