from PySide6.QtWidgets import QRadioButton, QButtonGroup, QCheckBox, QGroupBox, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy, QLineEdit, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCheckBox and QRadioButton")

        # Checkboxes: operating system

        os = QGroupBox("Choose operating system")

        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windows_box_toggled)

        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_box_toggled)

        mac = QCheckBox("Mac")
        mac.toggled.connect(self.windows_box_toggled)

        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)

        # Exclusive checkboxes: Drinks

        drinks = QGroupBox("Choose your drink")
        beer = QCheckBox("Beer")
        juice = QCheckBox("Juice")
        coffee = QCheckBox("Coffee")
        beer.setChecked(True)

        # Make the checkboxes exclusive

        exclusive_button_group = QButtonGroup(self) # self parent is needed here
        exclusive_button_group.addButton(beer) 
        exclusive_button_group.addButton(juice) 
        exclusive_button_group.addButton(coffee) 
        exclusive_button_group.setExclusive(True) 

        drink_layout = QVBoxLayout()
        drink_layout.addWidget(beer)
        drink_layout.addWidget(juice)
        drink_layout.addWidget(coffee)
        drinks.setLayout(drink_layout)
        
        # Radio buttons: answers
        
        answers = QGroupBox("Choose an Answer")
        answer_a = QRadioButton("A")
        answer_b = QRadioButton("B")
        answer_c = QRadioButton("C")
        answer_a.setChecked(True)

        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answer_a)
        answers_layout.addWidget(answer_b)
        answers_layout.addWidget(answer_c)
        answers.setLayout(answers_layout)


        h_layout = QHBoxLayout()
        h_layout.addWidget(os)
        h_layout.addWidget(drinks)
        
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(answers)

    
        self.setLayout(v_layout)

    def windows_box_toggled(self,checked):
        if(checked):
            print("Windows box checked")
        else:
            print("Windows box unchecked")
    
    def linux_box_toggled(self,checked):
        if(checked):
            print("Linux box checked")
        else:
            print("Linux box unchecked")
    
    def mac_box_toggled(self,checked):
        if(checked):
            print("Mac box checked")
        else:
            print("Mac box unchecked")
    