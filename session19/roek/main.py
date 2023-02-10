from functools import partial
import sys
import random
import time
from PySide6 import QtCore, QtGui
import PySide6
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *

from roek import Ui_MainWindow
class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        loadr=QUiLoader()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_paper.clicked.connect(partial(self.user_choice,'paper'))
        self.ui.btn_rock.clicked.connect(partial(self.user_choice,'rock'))
        self.ui.btn_scissors.clicked.connect(partial(self.user_choice,'scissors'))
        self.usr_score=0
        self.computer_score=0


    def user_choice(self,choice):
        im = QPixmap(f"img/{choice}.png")
        self.ui.lbl_user.setPixmap(im)
        self.user_choice=choice
        self.computer_choice()


    def computer_choice(self):
        self.cmptr_choice=random.choice(['paper','rock','scissors'])
        im = QPixmap(f"img/{self.cmptr_choice}.png")
        im=im.transformed(QtGui.QTransform().rotate(180))
        self.ui.lbl_cmptr.setPixmap(im)
        self.check_winner()

    def check_winner(self):
        if self.user_choice=='paper' and self.cmptr_choice=='paper' or self.user_choice=='rock' and self.cmptr_choice=='rock' or self.user_choice=='scissors' and self.cmptr_choice=='scissors':
            self.win='No body wins'

        elif self.user_choice=='paper' and self.cmptr_choice=='rock' or self.user_choice=='rock' and self.cmptr_choice=='scissors' or self.user_choice=='scissors' and self.cmptr_choice=='paper':
            self.win='User wins'
            self.usr_score+=1
        
        else:
            self.win='Computer wins'
            self.computer_score+=1
        
        
        self.ui.lbl_win.setText(self.win)
        self.ui.lbl_player_score.setText(f'Player score : {self.usr_score}')
        self.ui.lbl_computer_score.setText(f'Computer score : {self.computer_score}')
        self.check_end()
    
    def check_end(self):
        if self.usr_score == 10 or self.computer_score==10:
            if self.usr_score==10:
                self.ui.lbl_win.setText('you win')
            else:
                self.ui.lbl_win.setText('computer win')
            self.ui.centralwidget.setEnabled(False)
            


if __name__ == "__main__":
    app=QApplication([])
    window=Game()
    window.show()
    sys.exit(app.exec_())
