
import sys

from PySide6 import QtWidgets
from spinbox import Widget

app = QtWidgets.QApplication(sys.argv)

window = Widget()
window.show()

app.exec()


# for compiling, type this in the terminal: pyside6-uic {name of ui file from Qt Designer}.ui > ui_{name of ui file from Qt Designer}.py
# for resources, pyside6-rcc {name of resource file}.qrc -o {name of resource file}.py
# change from UTF-16 BE to UTF-8 
# for every change in QDesigner, always recompile