# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'namber.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(278, 428)
        Main.setStyleSheet(u"background-color: rgb(170, 0, 0);\n"
"alternate-background-color: rgb(170, 0, 0);")
        self.label = QLabel(Main)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 201, 41))
        font = QFont()
        font.setFamilies([u"IRANSansFaNum Black"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #FFF;")
        self.txt_input = QLineEdit(Main)
        self.txt_input.setObjectName(u"txt_input")
        self.txt_input.setGeometry(QRect(86, 80, 101, 91))
        font1 = QFont()
        font1.setFamilies([u"IRANSansFaNum Black"])
        font1.setPointSize(22)
        font1.setBold(True)
        self.txt_input.setFont(font1)
        self.txt_input.setStyleSheet(u"background-color: #FFF; border-radius: 10px; border: 0px;")
        self.txt_input.setAlignment(Qt.AlignCenter)
        self.btn_guess = QPushButton(Main)
        self.btn_guess.setObjectName(u"btn_guess")
        self.btn_guess.setGeometry(QRect(90, 190, 91, 41))
        self.btn_guess.setFont(font)
        self.btn_guess.setStyleSheet(u"color: #FFFF00;background-color: #FF1111; border-radius: 5px; border: 0px;")
        self.label_2 = QLabel(Main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 240, 41, 31))
        font2 = QFont()
        font2.setFamilies([u"IRANSansFaNum Black"])
        font2.setPointSize(10)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: #FFFF00;")
        self.lbl_joon = QLabel(Main)
        self.lbl_joon.setObjectName(u"lbl_joon")
        self.lbl_joon.setGeometry(QRect(100, 240, 21, 31))
        font3 = QFont()
        font3.setFamilies([u"IRANSansFaNum Black"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.lbl_joon.setFont(font3)
        self.lbl_joon.setStyleSheet(u"color: #FFF;")
        self.lbl_comment = QLabel(Main)
        self.lbl_comment.setObjectName(u"lbl_comment")
        self.lbl_comment.setGeometry(QRect(30, 290, 211, 41))
        self.lbl_comment.setFont(font3)
        self.lbl_comment.setStyleSheet(u"border: 0px; color: #FFF;")
        self.lbl_comment.setAlignment(Qt.AlignCenter)
        self.btn_new = QPushButton(Main)
        self.btn_new.setObjectName(u"btn_new")
        self.btn_new.setGeometry(QRect(90, 360, 91, 41))
        self.btn_new.setFont(font3)
        self.btn_new.setStyleSheet(u"color: #000; background-color: #FFF; border-radius: 5px; border: 0px;")

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.label.setText(QCoreApplication.translate("Main", u"\u06cc\u06a9 \u0639\u062f\u062f \u0627\u0632 10 \u062a\u0627 100 \u0627\u0646\u062a\u062e\u0627\u0628 \u06a9\u0646\u06cc\u062f", None))
        self.btn_guess.setText(QCoreApplication.translate("Main", u"\u062d\u062f\u0633\u062a \u0627\u0646\u062c\u0627\u0645 \u0634\u062f", None))
        self.label_2.setText(QCoreApplication.translate("Main", u"\u0627\u0645\u062a\u06cc\u0627\u0632", None))
        self.lbl_joon.setText("")
        self.lbl_comment.setText("")
        self.btn_new.setText(QCoreApplication.translate("Main", u"\u0634\u0631\u0648\u0639 \u062f\u0648\u0628\u0627\u0631\u0647 \u0628\u0627\u0632\u06cc", None))
    # retranslateUi

