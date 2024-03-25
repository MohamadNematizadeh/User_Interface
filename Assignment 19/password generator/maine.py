
import sys
import os
import random

from PySide6.QtWidgets import QApplication , QMainWindow
from PySide6.QtCore import QFile
from password import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generate.clicked.connect(self.GeneratePass)
        self.string = ''
    def GeneratePass(self):
        self.string = ''

        if self.ui.rdb_1.isChecked():
            uppercase = chr(random.randint(65, 90))
            special_char = chr(random.randint(33, 47))
            number = str(random.randint(0, 9))
            rand_list = random.sample(range(8), 3)

            for i in range(8):
                self.string = self.string + chr(random.randint(97, 122))

            self.string = list(self.string)
            self.string[rand_list[0]] = uppercase
            self.string[rand_list[1]] = special_char
            self.string[rand_list[2]] = number

        elif self.ui.rdb_2.isChecked():
            uppercase = random.sample(range(65, 90), 2)
            special_char = random.sample(range(33, 47), 2)
            number = random.sample(range(0, 9), 2)
            rand_list = random.sample(range(12), 6)

            for i in range(12):
                self.string = self.string + chr(random.randint(97, 122))

            self.string = list(self.string)
            self.string[rand_list[0]] = chr(uppercase[0])
            self.string[rand_list[1]] = chr(uppercase[1])
            self.string[rand_list[2]] = chr(special_char[0])
            self.string[rand_list[3]] = chr(special_char[1])
            self.string[rand_list[4]] = str(number[0])
            self.string[rand_list[5]] = str(number[1])

        elif self.ui.rdb_3.isChecked():
            uppercase = random.sample(range(65, 90), 3)
            special_char = random.sample(range(33, 47), 2)
            number = random.sample(range(0, 9), 3)
            rand_list = random.sample(range(20), 8)

            for i in range(20):
                self.string = self.string + chr(random.randint(97, 122))

            self.string = list(self.string)
            self.string[rand_list[0]] = chr(uppercase[0])
            self.string[rand_list[1]] = chr(uppercase[1])
            self.string[rand_list[2]] = chr(uppercase[2])
            self.string[rand_list[3]] = chr(special_char[0])
            self.string[rand_list[4]] = chr(special_char[1])
            self.string[rand_list[5]] = str(number[0])
            self.string[rand_list[6]] = str(number[1])
            self.string[rand_list[7]] = str(number[2])

        self.string = "".join(list(self.string))
        self.ui.txt_result.setText(self.string)

     
app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())