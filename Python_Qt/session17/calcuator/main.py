import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QPixmap, QImage

chek=0
def ico():
    main_window.btn_play.setIcon(QIcon('icon/icons8-calculator-64.png'))
# nambers.-.-.-.-.-.-.-.-
def namber1():
    main_window.textbox.setText(main_window.textbox.text()+'1')
def namber2():
    main_window.textbox.setText(main_window.textbox.text()+'2')
def namber3():
    main_window.textbox.setText(main_window.textbox.text()+'3')
def namber4():
    main_window.textbox.setText(main_window.textbox.text()+'4')
def namber5():
    main_window.textbox.setText(main_window.textbox.text()+'5')
def namber6():
    main_window.textbox.setText(main_window.textbox.text()+'6')
def namber7():
    main_window.textbox.setText(main_window.textbox.text()+'7')
def namber8():
    main_window.textbox.setText(main_window.textbox.text()+'8')
def namber9():
    main_window.textbox.setText(main_window.textbox.text()+'9')
def namber0():
    main_window.textbox.setText(main_window.textbox.text()+'0')
    
def btn_sum():
    global a
    global cehk
    cehk = '+'
    a = float(main_window.textbox.text())
    main_window.textbox.setText('')  
    
def btn_sub():
    global a
    global cehk
    cehk = '-'
    a = float(main_window.textbox.text())
    main_window.textbox.setText('')
    
def btn_mul():
    global a
    global cehk
    cehk = '*'
    a = float(main_window.textbox.text())
    main_window.textbox.setText('')
    
def btn_dev():
    global a
    global cehk
    cehk = '/'
    a = float(main_window.textbox.text())
    main_window.textbox.setText('')
def btn_equal():
    global b
    b = float(main_window.textbox.text())
    if cehk in globals():
        if cehk == '+':
            b = a + b
        elif cehk == '-':
            b = a - b
        elif cehk == '*':
            b = a * b
        elif cehk == '/':
            b = a / b
        else:
            b = 0
    main_window.textbox.setText(str(b))  

def Ca():
    main_window.textbox.setText('')

def Sin():
    main_window.textbox.setText(str(math.sin(float(main_window.textbox.text()))))    

def Cos():
    main_window.textbox.setText(str(math.cos(float(main_window.textbox.text()))))
    
def Tan():
    main_window.textbox.setText(str(math.tan(float(main_window.textbox.text()))))
    
def Cot():
    main_window.textbox.setText(str(1/math.tan(float(main_window.textbox.text()))))
    
def Log():
    main_window.textbox.setText(str(math.log(float(main_window.textbox.text()))))
    
def Sqrt():
    main_window.textbox.setText(str(math.sqrt(float(main_window.textbox.text()))))
    


# loader_app.-.-.-.-.-.-.-.-
app_c = QApplication([])
loader = QUiLoader()
main_window = loader.load("calcuator.ui")
main_window.show()
# clicked.nambers.-.-.-.-.-.-.-.-
main_window.namber0.clicked.connect(namber0)
main_window.namber1.clicked.connect(namber1)
main_window.namber2.clicked.connect(namber2)
main_window.namber3.clicked.connect(namber3)
main_window.namber4.clicked.connect(namber4)
main_window.namber5.clicked.connect(namber5)
main_window.namber6.clicked.connect(namber6)
main_window.namber7.clicked.connect(namber7)
main_window.namber8.clicked.connect(namber8)
main_window.namber9.clicked.connect(namber9)
# btn_sum
main_window.btn_sum.clicked.connect(btn_sum)
main_window.btn_sub.clicked.connect(btn_sub)
main_window.btn_mul.clicked.connect(btn_mul)
main_window.btn_div.clicked.connect(btn_dev)

main_window.btn_equal.clicked.connect(btn_equal)
main_window.Ca.clicked.connect(Ca)
main_window.Sin.clicked.connect(Sin)
main_window.Cos.clicked.connect(Cos)
main_window.Tan.clicked.connect(Tan)
main_window.Cot.clicked.connect(Cot)
main_window.Log.clicked.connect(Log)
main_window.Sqrt.clicked.connect(Sqrt)
# main_window.btn_play.setIcon(QIcon('icon/icons8-calculator-64.png'))


app_c.exec()    
