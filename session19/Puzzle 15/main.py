
import sys
import random
from functools import partial

from functions import get_non_repeating_random_2d_list
from functools import partial
from PySide6.QtWidgets import QApplication,QMainWindow,QMessageBox
from puzzle15 import Ui_MainWindow
def get_non_repeating_random_2d_list(n, m): 
  
    # Create an empty list 
    matrix = [] 
  
    # Create a list containing n*m numbers from 1 to n*m 
    # and shuffle it to get random permutation of numbers 
    nums = list(range(1, n * m + 1)) 
    random.shuffle(nums) 

    # Fill the empty list with shuffled numbers 
    for i in range(n): 

        # Create an empty sublist  
        row = []  

        for j in range(m):  

            # Get the last number from nums list and append it to row sublist.  
            row.append(nums.pop())  

        # Append the row sublist to matrix list.  
        matrix.append(row)  

    return matrix

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        self.buttons = [[self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4],
                        [self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8],
                        [self.ui.btn_9, self.ui.btn_10, self.ui.btn_11, self.ui.btn_12],
                        [self.ui.btn_13, self.ui.btn_14, self.ui.btn_15, self.ui.btn_16]]
        my_list =get_non_repeating_random_2d_list(4, 4)  
        for i in range(4):
            for j in range(4):
                rand_number = my_list[i][j]
                self.buttons[i][j].setText(str(rand_number))
                self.buttons[i][j].clicked.connect(partial(self.play, i, j))
                if rand_number == 16:
                    self.buttons[i][j].setVisible(False)
                    self.empty_i = i 
                    self.empty_j = j 
    def play(self, i, j):
        if (i == self.empty_i and abs(j - self.empty_j) == 1) or\
              (j == self.empty_j and abs(i - self.empty_i) == 1):
            self.buttons[self.empty_i][self.empty_j].setText(self.buttons[i][j].text())
            self.buttons[i][j].setText("16")
            self.buttons[self.empty_i][self.empty_j].setVisible(True)
            self.buttons[i][j].setVisible(False)
            self.empty_i = i 
            self.empty_j = j
        if self.check() == True :
            msg_box = QMessageBox()
            msg_box.setText("شما برنده شدید")    
            msg_box.exec()

    def check(self):
        index = 1
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text()) != index:
                    return False
                index += 1
        return True              
app = QApplication(sys.argv)    
main_window = MainWindow()
main_window.show()
app.exec()