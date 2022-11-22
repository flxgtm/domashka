import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont, QIcon
import random


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("камень ножницы бумага")
        self.resize(700, 300) 
        self.setWindowIcon(QIcon('icon.png'))
        self.setFont(QFont('Georgia', 20))      

    def initUI(self):
  
        label1 = QLabel("rock paper scissors", self)

        font = QFont('Times', 15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        label1.setFont(font)
        label1.setAlignment(Qt.AlignCenter)
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.darkCyan)
        label1.setGraphicsEffect(color)

        self.who = QLabel("who wins?")
        self.who.setAlignment(Qt.AlignCenter)
        font.setUnderline(False)
        font.setItalic(False)
        self.who.setFont(font)
        
        self.computer = QLabel()

        self.winner = QLabel()
        self.winner.setFont(QFont('Georgia', 20))
        self.winner.setGeometry(120, 270, 80, 35)
        self.winner.setStyleSheet("border : 2px solid black; background : white;")
        self.winner.setAlignment(Qt.AlignCenter)
        
        self.rock = QPushButton("Rock", self)
        self.rock.setGeometry(30, 270, 80, 35)

        self.paper = QPushButton("Paper", self)
        self.paper.setGeometry(120, 270, 80, 35)

        self.scissor = QPushButton("Scissors", self)
        self.scissor.setGeometry(210, 270, 80, 35)

        self.rock.clicked.connect(self.rock_action)
        self.paper.clicked.connect(self.paper_action)
        self.scissor.clicked.connect(self.scissor_action)

        game_play = QPushButton("PLAY!")
        game_play.setGeometry(100, 320, 120, 50)
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.red)
        game_play.setGraphicsEffect(color)
        game_play.clicked.connect(self.play_action)
        
        self.rock.setDisabled(True)
        self.paper.setDisabled(True)
        self.scissor.setDisabled(True)        

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(self.who)
        layout.addWidget(self.winner)
        layout.addWidget(self.computer)

        layout.addWidget(self.rock)
        layout.addWidget(self.paper)
        layout.addWidget(self.scissor)
        layout.addWidget(game_play)

        self.setLayout(layout)
                  
    #камень-ножницы, камень-бумага, ножницы-бумага
    def rock_action(self):
        self.rock.setDisabled(True)
        self.paper.setDisabled(True)
        self.scissor.setDisabled(True)      
        
        if self.cho == 'both':
            self.winner.setText('It\'s a tie')
        elif self.cho == 'computer':
            self.winner.setText('YOU lose, computer has chosen paper')         
        else:
            self.winner.setText('YOU WON YIPPEEE')
            
    def paper_action(self):
        self.rock.setDisabled(True)
        self.paper.setDisabled(True)
        self.scissor.setDisabled(True)
             
        if self.cho == 'both':
            self.winner.setText('It\'s a tie')
        elif self.cho == 'computer':
            self.winner.setText('YOU lose, computer has chosen scissors')          
        else:
            self.winner.setText('YOU WON YIPPEEE')        
        
    def scissor_action(self):
        self.rock.setDisabled(True)
        self.paper.setDisabled(True)
        self.scissor.setDisabled(True)
        
        if self.cho == 'both':
            self.winner.setText('It\'s a tie')
        elif self.cho == 'computer':
            self.winner.setText('YOU lose, computer has chosen rock')         
        else:
            self.winner.setText('YOU WON YIPPEEE')          
        
    
    def play_action(self):
        self.winner.setText("")
        
        self.variants = ['computer', 'you', 'both']
        self.cho = random.choice(self.variants) 
        
        self.rock.setEnabled(True)
        self.paper.setEnabled(True)
        self.scissor.setEnabled(True)


def open_window():
    app = QApplication(sys.argv) 
    wind = Window()
    wind.show()
    sys.exit(app.exec_())
                                
open_window()