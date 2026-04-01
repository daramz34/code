import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QGridLayout, QHBoxLayout, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 200, 500, 500)
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
        layout = QGridLayout()

        central_widgit.setLayout(layout)


        # Screen
        self.display = QLabel("0000")
        self.display.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.display, 0, 0,1,4)
        #self.button1.setObjectName("button1")

        #numbers
        layout.addWidget(self.button1, 2,0)
        layout.addWidget(self.button2, 2,1)
        layout.addWidget(self.button3, 2,2)
        layout.addWidget(self.button4, 3,0)
        layout.addWidget(self.button5, 3,1)
        layout.addWidget(self.button6, 3,2)
        layout.addWidget(self.button7, 4,0)
        layout.addWidget(self.button8, 4,1)
        layout.addWidget(self.button9, 4,2)
        layout.addWidget(self.button10, 5,1)

        # # operations
        layout.addWidget(self.button11, 1,3)
        layout.addWidget(self.button12, 2,3)
        layout.addWidget(self.button13, 3,3)
        layout.addWidget(self.button14, 1,2)
        layout.addWidget(self.button15, 4,3)
        layout.addWidget(self.button16, 1,0)
        layout.addWidget(self.button17, 1,1)



        self.setStyleSheet(
            """QPushButton {
            background-color:  black;
            color: white; 
            font-size: 50px;
            }
            QLabel{
            padding: 20px;
            font-weight: bold;
            font-size: 50px;
            }
        
        
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()