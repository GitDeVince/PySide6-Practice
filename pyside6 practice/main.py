from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from mainwindow import MainWindow
from rockwidget import RocWidget

app = QApplication(sys.argv)

window = MainWindow(app)

#start the event loop
window.show()
app.exec()