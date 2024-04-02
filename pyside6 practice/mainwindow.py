from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
#based on notepad menubar

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app # declare an app member
        self.setWindowTitle("Custom MainWindow")

        #menubar and menus
        menu_bar = self.menuBar()

        # under file
        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction("New Tab")
        file_menu.addAction("New Window")
        file_menu.addAction("Open")
        file_menu.addAction("Save")
        file_menu.addAction("Save As")
        file_menu.addAction("Save All")
        file_menu.addAction("Page Setup")
        file_menu.addAction("Print")
        file_menu.addAction("Close Tab")
        file_menu.addAction("Close Window")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        # under edit
        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Delete")
        edit_menu.addAction("Find")
        edit_menu.addAction("Find Next")
        edit_menu.addAction("Find Previous")
        edit_menu.addAction("Replace")
        edit_menu.addAction("Go To")
        edit_menu.addAction("Select All")
        edit_menu.addAction("Time/Date")
        edit_menu.addAction("Font")


        # under view 
        view_menu = menu_bar.addMenu("&View")
        view_menu.addAction("Zoom")
        view_menu.addAction("Status Bar")
        view_menu.addAction("Word Wrap")
        
        # toolbar
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        # adding quit action in toolbar
        toolbar.addAction(quit_action)

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("placeholder.png"), "Some other action", self)
        action2.setStatusTip("Status message for other action")
        action2.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action2)

        # status bar
        self.setStatusBar(QStatusBar(self))



    def quit_app(self):
        self.app.quit()


    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app", 3000)
        