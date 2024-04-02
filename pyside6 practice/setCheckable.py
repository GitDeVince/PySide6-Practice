from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

def button_clicked(data):
    print("You Clicked. State: ", data)


app = QApplication(sys.argv)
button = QPushButton("Press Me")
button.setCheckable(True)

button.clicked.connect(button_clicked)
#start the event loop
button.show()
app.exec()