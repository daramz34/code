import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QGridLayout, QHBoxLayout, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 200, 500, 500)
        self.setWindowTitle("CALCULATOR APP")
        # numbers
        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")
        self.button4 = QPushButton("4")
        self.button5 = QPushButton("5")
        self.button6 = QPushButton("6")
        self.button7 = QPushButton("7")
        self.button8 = QPushButton("8")
        self.button9 = QPushButton("9")
        self.button10 = QPushButton("0")

        # operations
        self.button11 = QPushButton("+")
        self.button12 = QPushButton("-")
        self.button13 = QPushButton("x")
        self.button14 = QPushButton("/")
        self.button15 = QPushButton("=")

        #specials
        self.button16 = QPushButton("C")
        self.button17 = QPushButton("⌫")

        self.InitUI()

    def InitUI(self):
        central_widgit = QWidget()
        self.setCentralWidget(central_widgit)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10,10)
        central_widgit.setLayout(layout)


        # Screen
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setFixedHeight(100)
        layout.addWidget(self.display)
        #self.button1.setObjectName("button1")


        #buttons
        button_grid = QGridLayout()
        button_grid.setSpacing(8)
        layout.addLayout(button_grid)
        #numbers
        button_grid.addWidget(self.button16, 0, 0)
        button_grid.addWidget(self.button17, 0, 1)
        button_grid.addWidget(self.button14, 0, 2)
        button_grid.addWidget(self.button11, 0, 3)

        button_grid.addWidget(self.button1, 1, 0)
        button_grid.addWidget(self.button2, 1, 1)
        button_grid.addWidget(self.button3, 1, 2)
        button_grid.addWidget(self.button12, 1, 3)

        button_grid.addWidget(self.button4, 2, 0)
        button_grid.addWidget(self.button5, 2, 1)
        button_grid.addWidget(self.button6, 2, 2)
        button_grid.addWidget(self.button13, 2, 3)

        button_grid.addWidget(self.button7, 3, 0)
        button_grid.addWidget(self.button8, 3, 1)
        button_grid.addWidget(self.button9, 3, 2)
        button_grid.addWidget(self.button15, 3, 3)

        button_grid.addWidget(self.button10, 4, 0, 1,3)
       
        



        self.setStyleSheet(
            """QPushButton {
            background-color:  #333333;
            color: white; 
            font-size: 20px;
            border-radius: 10px;
            min-height: 70px;
            }
            QLabel{
            background-color: #1c1c1c;
            padding: 15px;
            font-size: 50px;
            color: rgba(255,255,255,0.3);
            }
            QPushButton:pressed {
            background-color: #555555;
            border: 2px solid brown;
            }
            QPushButton:hover{
            background-color: #444444;
            }

            QMainWindow{
            background-color: #121212;
            }
            QPushButton#operator{
                background-color: #FF9500;
               
            }
        
        
        """)
        


        number_buttons = [self.button1, self.button2, self.button3, self.button4, self.button5,
                          self.button6, self.button7, self.button8, self.button9, self.button10]
        
        for btn in number_buttons:
            btn.clicked.connect(self.handle_number)


        opertions_buttons = [self.button11, self.button12, self.button13, self.button14]

        for op_btn in opertions_buttons:
            op_btn.clicked.connect(self.handle_operations)
        
        for op_btn in opertions_buttons:
            op_btn.setObjectName("operator")

        self.button15.clicked.connect(self.calculate_result)
        self.button16.clicked.connect(self.clear_everything)
        self.button17.clicked.connect(self.handle_backspace)
    

    
    
    def handle_number(self):
         # sender tells us exactly which button was clicked
         button = self.sender()

         current_text = self.display.text()

         if current_text == "0":
             self.display.setText(button.text())
             self.display.setStyleSheet("color: rgba(255,255,255,1.0)")
         else:
             self.display.setText(current_text + button.text())
    

    def handle_operations(self):
        operations = self.sender()

        current_text = self.display.text()

        if current_text == "0" and operations.text() != "-":
            return
        
        symbol = operations.text()
        if current_text == "0":
            self.display.setText(symbol)
            self.display.setStyleSheet("color: rgba(255,255,255,1.0)")
        self.display.setText(current_text + symbol)

    def calculate_result(self):
        try:

            Text = self.display.text()
            Text = Text.replace('x', '*')

            result = eval(Text)
            self.display.setText(str(result))
        
        except Exception:
            self.display.setText("Error")
    

    def clear_everything(self):
        self.display.setText("0")
        # Reset to dimmed look
        self.display.setStyleSheet("color: rgba(255, 255, 255, 0.3);")
    
    def handle_backspace(self):
        current_text = self.display.text()


        if len(current_text) <= 1 or current_text == "0":
            self.display.setText("0")
            self.display.setStyleSheet("color: rgba(255, 255, 255, 0.3);")
        
        else:
            new_text = current_text[:-1]
            self.display.setText(new_text)


        

        
            



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()