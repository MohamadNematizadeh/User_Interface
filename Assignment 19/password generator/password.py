# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'password.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(488, 534)
        MainWindow.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/app-icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #121212;\n"
"    color: white;\n"
"    font-family: Verdana;\n"
"    font-size: 16pt;\n"
"    margin: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_lower,\n"
"#btn_upper,\n"
"#btn_digits,\n"
"#btn_special {\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: #090;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid #090;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #006300;\n"
"    border-color: #090;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.layout_password = QHBoxLayout()
        self.layout_password.setObjectName(u"layout_password")
        self.txt_result = QTextEdit(self.centralwidget)
        self.txt_result.setObjectName(u"txt_result")
        self.txt_result.setMaximumSize(QSize(16777215, 35))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(16)
        self.txt_result.setFont(font)
        self.txt_result.setStyleSheet(u"background-color: #FFF; border-radius: 5px; border: 0px solid; margin: 0px 10px;\n"
"color: rgb(0, 0, 0);")

        self.layout_password.addWidget(self.txt_result)

        self.btn_generate = QPushButton(self.centralwidget)
        self.btn_generate.setObjectName(u"btn_generate")

        self.layout_password.addWidget(self.btn_generate)


        self.verticalLayout.addLayout(self.layout_password)

        self.rdb_1 = QPushButton(self.centralwidget)
        self.rdb_1.setObjectName(u"rdb_1")
        self.rdb_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.rdb_1.setCheckable(True)
        self.rdb_1.setChecked(True)

        self.verticalLayout.addWidget(self.rdb_1)

        self.rdb_2 = QPushButton(self.centralwidget)
        self.rdb_2.setObjectName(u"rdb_2")
        self.rdb_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.rdb_2.setCheckable(True)

        self.verticalLayout.addWidget(self.rdb_2)

        self.rdb_3 = QPushButton(self.centralwidget)
        self.rdb_3.setObjectName(u"rdb_3")
        self.rdb_3.setFont(font)
        self.rdb_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.rdb_3.setCheckable(True)
        self.rdb_3.setChecked(True)

        self.verticalLayout.addWidget(self.rdb_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.txt_result.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Verdana'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.rdb_1.setText(QCoreApplication.translate("MainWindow", u"Generate a Standard Strength Password\n"
"", None))
        self.rdb_2.setText(QCoreApplication.translate("MainWindow", u"Generate a Super Strong Password\n"
"", None))
        self.rdb_3.setText(QCoreApplication.translate("MainWindow", u"Generate an Extra Strong Password", None))
    # retranslateUi

