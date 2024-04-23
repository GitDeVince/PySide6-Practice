from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __init__(self, app):
        self.app = app
        super().__init__()

        self.setWindowTitle("QMessageBox")

        button_quit = QPushButton("Quit")
        button_quit.clicked.connect(self.button_clicked_quit)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        # set up layout
        layout = QVBoxLayout()
        layout.addWidget(button_quit)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)

    def button_clicked_quit(self):
        ret = QMessageBox.critical(self, "Shutting Down", "Are you sure to close the Program?",  QMessageBox.Ok | QMessageBox.Cancel )
        if ret == QMessageBox.Ok :
            self.app.quit()
        

    def button_clicked_critical(self):
        print("critical")
    def button_clicked_question(self):
        print("question")
    def button_clicked_information(self):
        print("information")
    def button_clicked_warning(self):
        print("warning")
    def button_clicked_about(self):
        print("about")