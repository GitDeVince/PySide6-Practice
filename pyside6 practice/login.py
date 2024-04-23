from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, QLineEdit, QLabel


# a place to accept username and password. 
#checks if its in data storage
# if yes, pop up message will appear saying "login accepted". if no, pop up message will show a warning

class Widget(QWidget):
    def __init__(self, employee_data):
        super().__init__()

        self.employee_data = employee_data # accessing the dictionary 
        self.setWindowTitle("Login System")

        email_label = QLabel("Email : ")
        password_label = QLabel("Password : ")

        self.email_edit = QLineEdit()
        self.password_edit = QLineEdit()

        button = QPushButton("Confirm")
        button.clicked.connect(self.complete_info_check) # checking if email and password is not empty
        button.clicked.connect(self.validation) # checking if inputed by user is in the data storage

        h_layout = QHBoxLayout()
        h_layout.addWidget(email_label)
        h_layout.addWidget(self.email_edit)

        h_layout.addWidget(password_label)
        h_layout.addWidget(self.password_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)

        self.setLayout(v_layout)


    def validation(self):
        email_value = self.email_edit.text()
        password_value = self.password_edit.text()

        email_found = False
        password_found = False

        for name, data in employee_data.items():
            if 'email' in data and data['email'] == email_value:
                email_found = True
            if 'password' in data and data['password'] == password_value:
                password_found = True
        
        if email_found and password_found:
            QMessageBox.information(self, "Access Granted", "You are now login to the system.",  QMessageBox.Ok)
            print("good")
        else:
            QMessageBox.critical(self, "Login Error", "Wrong Information inputed. Please try again.",  QMessageBox.Ok)
            print("bad")

    def complete_info_check(self):
        email_value = self.email_edit.text()
        password_value = self.password_edit.text()

        if not email_value and not password_value:
            QMessageBox.critical(self, "Login Error", "Email address and password is missing. Please enter your information.",  QMessageBox.Ok)
            print("bad")

        else:

            if not email_value:
                QMessageBox.critical(self, "Login Error", "Please enter your email address.",  QMessageBox.Ok)
                print("bad")
            elif not password_value:
                QMessageBox.critical(self, "Login Error", "Please enter your password.",  QMessageBox.Ok)
                print("bad")

employee_data = {
    'Reymark Gonzales': {'email': "reymark10@yahoo.com", 'password': "12345"},
    'Betty Reyes': {'email': 'bettyreyes@gmail.com', 'password': "@bettyR"}
}
