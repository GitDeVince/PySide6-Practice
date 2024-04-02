from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

def respond_to_slider(data):
    print("Slider moved to : ", data) # responds when something happens

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(50)

slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()