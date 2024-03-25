import random
import sys
from functools import partial
from PySide6.QtWidgets import QApplication , QMessageBox
from PySide6.QtUiTools import QUiLoader
player_score = 0
player2_score = 0
def check(): 
        if ((buttons[0][0].text() == "X" and buttons[1][1].text() == "X" and buttons[2][2].text() == "X") or (buttons[0][2].text() == "X" and buttons[1][1].text() == "X" and buttons[2][0].text() == "X") or (buttons[0][0].text() == "X" and buttons[0][1].text() == "X" and buttons[0][2].text() == "X") or (buttons[1][0].text() == "X" and buttons[1][1].text() == "X" and buttons[1][2].text() == "X") or (buttons[2][0].text() == "X" and buttons[2][1].text() == "X" and buttons[2][2].text() == "X") or (buttons[0][0].text() == "X" and buttons[1][0].text() == "X" and buttons[2][0].text() == "X") or (buttons[0][1].text() == "X" and buttons[1][1].text() == "X" and buttons[2][1].text() == "X") or (buttons[0][2].text() == "X" and buttons[1][2].text() == "X" and buttons[2][2].text() == "X")):
            global player_score
            global player2_score
            player_score += 1
            ms_box = QMessageBox()
            ms_box.setText("player 1 wins")
            main_window.scorex.setText(str(player_score))
            ms_box.exec()
            new_game()
        elif ((buttons[0][0].text() == "O" and buttons[1][1].text() == "O" and buttons[2][2].text() == "O") or (buttons[0][2].text() == "O" and buttons[1][1].text() == "O" and buttons[2][0].text() == "O") or (buttons[0][0].text() == "O" and buttons[0][1].text() == "O" and buttons[0][2].text() == "O") or (buttons[1][0].text() == "O" and buttons[1][1].text() == "O" and buttons[1][2].text() == "O") or (buttons[2][0].text() == "O" and buttons[2][1].text() == "O" and buttons[2][2].text() == "O") or (buttons[0][0].text() == "O" and buttons[1][0].text() == "O" and buttons[2][0].text() == "O") or (buttons[0][1].text() == "O" and buttons[1][1].text() == "O" and buttons[2][1].text() == "O") or (buttons[0][2].text() == "O" and buttons[1][2].text() == "O" and buttons[2][2].text() == "O")):
            player2_score += 1
            ms_box = QMessageBox()
            ms_box.setText("player2 win")
            main_window.scoreo.setText(str(player2_score))
            ms_box.exec()
            new_game()
        if buttons[0][0].text() != "" and buttons[0][1].text() != "" and buttons[0][2].text() != "" and buttons[1][0].text() != "" and buttons[1][1].text() != "" and buttons[1][2].text() != "" and buttons[2][0].text() != "" and buttons[2][1].text() != "" and buttons[2][2].text() != "":
            ms_box = QMessageBox()
            ms_box.setText("draw")
            ms_box.exec()
            new_game()
player = "X"
def play(i, j):
        if buttons[i][j].text() == "":
            global player
            if main_window.btn_ptp.isChecked():
                if player == "X":
                    buttons[i][j].setText("X")
                    buttons[i][j].setStyleSheet("color:read; background-color : pink;")
                    player = "O"
                else:
                    buttons[i][j].setText("O")
                    buttons[i][j].setStyleSheet("color:blue; background-color : lightblue;")
                    player = "X"
            if main_window.btn_ptc.isChecked():
                if player == "X":
                    buttons[i][j].setText("X")
                    buttons[i][j].setStyleSheet("color:read; background-color : pink;")
                    player = "O"
                if player == "O":
                    while True:
                        i = random.randint(0, 2)
                        j = random.randint(0, 2)
                        if buttons[i][j].text() == "":
                            buttons[i][j].setText("O")
                            buttons[i][j].setStyleSheet("color:blue; background-color : lightblue;")
                            player = "X"
                            break
        check()
def new_game():
        for i in range(3):
            for j in range(3):
                buttons[i][j].setStyleSheet("background-color:rgb(255, 255, 255);")
                buttons[i][j].setText("") 
def about():
        ms_box = QMessageBox()
        ms_box.setText("Tic-Tac-Toe vi 1\n This Game using Pyside6\nprogram was developed by:\nmohmmad@gmail.com")
        ms_box.exec()                
app =QApplication(sys.argv)
player = 1
loader = QUiLoader()
main_window =loader.load("TicTacToe.ui")
main_window.show()
buttons =[[main_window.btn_1,main_window.btn_2,main_window.btn_3],
        [main_window.btn_4,main_window.btn_5,main_window.btn_6],
        [main_window.btn_7,main_window.btn_8,main_window.btn_9]]

for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play,i,j))

main_window.btn_new.clicked.connect(new_game)
main_window.btn_abt.clicked.connect(about)
app.exec()