from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout
import sys



class RocWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")

        #everytime it clicks, function that is for the specified button will print a string

        button1 = QPushButton("Button1")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Button2")
        button2.clicked.connect(self.button2_clicked)

        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        self.setLayout(button_layout)
        
    def button1_clicked(self):
        print("You clicked button1")

    def button2_clicked(self):
        print("You clicked button2")