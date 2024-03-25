import sys
import os
import random
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from namber import Ui_Main
class  Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.ui.btn_guess.clicked.connect(self.guess)
        self.ui.btn_new.clicked.connect(self.new_game)
        self.number = random.randint(1, 100)
        self.score = 10
        self.ui.lbl_joon.setText(str(self.score))
        print(self.number)
    def guess(self):
        if self.ui.txt_input.text().isnumeric():
            
            if int(self.ui.txt_input.text()) == self.number:
                self.ui.lbl_comment.setText('شما برنده شدید ایول')
                
            elif int(self.ui.txt_input.text()) > self.number:
                self.score -= 1
                if self.score == 0:
                    self.ui.lbl_comment.setText('🤦‍♀️چرا نتوانستی تشخیص بدی وای')
                    self.new_game()
                else:
                    self.ui.lbl_comment.setText('لطفا  بیرین پاین تر')
            else:
                self.score -= 1
                if self.score == 0:
                    self.ui.lbl_comment.setText('🤦‍♀️چرا نتوانستی تشخیص بدی وای')
                    self.new_game()
                else:
                    self.ui.lbl_comment.setText(' لطفا  برین  بالا تر ')
            self.ui.lbl_joon.setText(str(self.score))
        else:
            msg_box = QMessageBox()
            msg_box.setText("دادچ عدد رو وارد کن")
            msg_box.exec_()
    
    def new_game(self):
        self.number = random.randint(1, 100)
        self.score = 10
        self.ui.txt_input.setText('')
        self.ui.lbl_joon.setText(str(self.score))
                

if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    widget.show()
    sys.exit(app.exec_())