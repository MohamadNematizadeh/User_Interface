# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'from2.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(339, 524)
        MainWindow.setStyleSheet(u"background-color: rgb(47, 153, 174);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.layout_password_2 = QHBoxLayout()
        self.layout_password_2.setObjectName(u"layout_password_2")
        self.lbl_player_score = QLabel(self.centralwidget)
        self.lbl_player_score.setObjectName(u"lbl_player_score")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_player_score.sizePolicy().hasHeightForWidth())
        self.lbl_player_score.setSizePolicy(sizePolicy)
        self.lbl_player_score.setStyleSheet(u"font: 900 11pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.lbl_player_score.setAlignment(Qt.AlignCenter)

        self.layout_password_2.addWidget(self.lbl_player_score)

        self.lbl_user = QLabel(self.centralwidget)
        self.lbl_user.setObjectName(u"lbl_user")
        self.lbl_user.setStyleSheet(u"border-color: rgb(255, 255, 127);\n"
"border-style: dashed;\n"
"border-width: 5px;")
        self.lbl_user.setAlignment(Qt.AlignCenter)

        self.layout_password_2.addWidget(self.lbl_user)


        self.gridLayout.addLayout(self.layout_password_2, 3, 0, 1, 1)

        self.layout_password_3 = QHBoxLayout()
        self.layout_password_3.setObjectName(u"layout_password_3")
        self.btn_scissors = QPushButton(self.centralwidget)
        self.btn_scissors.setObjectName(u"btn_scissors")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_scissors.sizePolicy().hasHeightForWidth())
        self.btn_scissors.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.btn_scissors.setFont(font)
        self.btn_scissors.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")
        icon = QIcon()
        icon.addFile(u"images/scissors.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_scissors.setIcon(icon)
        self.btn_scissors.setIconSize(QSize(60, 60))

        self.layout_password_3.addWidget(self.btn_scissors)

        self.btn_rock = QPushButton(self.centralwidget)
        self.btn_rock.setObjectName(u"btn_rock")
        sizePolicy1.setHeightForWidth(self.btn_rock.sizePolicy().hasHeightForWidth())
        self.btn_rock.setSizePolicy(sizePolicy1)
        self.btn_rock.setFont(font)
        self.btn_rock.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")
        icon1 = QIcon()
        icon1.addFile(u"images/rock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rock.setIcon(icon1)
        self.btn_rock.setIconSize(QSize(60, 60))

        self.layout_password_3.addWidget(self.btn_rock)

        self.btn_paper = QPushButton(self.centralwidget)
        self.btn_paper.setObjectName(u"btn_paper")
        sizePolicy1.setHeightForWidth(self.btn_paper.sizePolicy().hasHeightForWidth())
        self.btn_paper.setSizePolicy(sizePolicy1)
        self.btn_paper.setFont(font)
        self.btn_paper.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")
        icon2 = QIcon()
        icon2.addFile(u"images/paper.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_paper.setIcon(icon2)
        self.btn_paper.setIconSize(QSize(60, 60))

        self.layout_password_3.addWidget(self.btn_paper)


        self.gridLayout.addLayout(self.layout_password_3, 4, 0, 1, 1)

        self.lbl_win = QLabel(self.centralwidget)
        self.lbl_win.setObjectName(u"lbl_win")
        sizePolicy.setHeightForWidth(self.lbl_win.sizePolicy().hasHeightForWidth())
        self.lbl_win.setSizePolicy(sizePolicy)
        self.lbl_win.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 0, 0);")
        self.lbl_win.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_win, 2, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(28, 20, 70);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.layout_password = QHBoxLayout()
        self.layout_password.setSpacing(19)
        self.layout_password.setObjectName(u"layout_password")
        self.lbl_cmptr = QLabel(self.centralwidget)
        self.lbl_cmptr.setObjectName(u"lbl_cmptr")
        self.lbl_cmptr.setStyleSheet(u"border-color: rgb(255, 255, 127);\n"
"border-style: dashed;\n"
"border-width: 5px;")
        self.lbl_cmptr.setAlignment(Qt.AlignCenter)

        self.layout_password.addWidget(self.lbl_cmptr)

        self.lbl_computer_score = QLabel(self.centralwidget)
        self.lbl_computer_score.setObjectName(u"lbl_computer_score")
        sizePolicy.setHeightForWidth(self.lbl_computer_score.sizePolicy().hasHeightForWidth())
        self.lbl_computer_score.setSizePolicy(sizePolicy)
        self.lbl_computer_score.setStyleSheet(u"font: 900 11pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.lbl_computer_score.setAlignment(Qt.AlignCenter)

        self.layout_password.addWidget(self.lbl_computer_score)


        self.gridLayout.addLayout(self.layout_password, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 339, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_player_score.setText(QCoreApplication.translate("MainWindow", u"Player : 0", None))
        self.lbl_user.setText("")
        self.btn_scissors.setText(QCoreApplication.translate("MainWindow", u"paper", None))
        self.btn_rock.setText(QCoreApplication.translate("MainWindow", u"rock", None))
        self.btn_paper.setText(QCoreApplication.translate("MainWindow", u"scissors", None))
        self.lbl_win.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rock Paper Scissors", None))
        self.lbl_cmptr.setText("")
        self.lbl_computer_score.setText(QCoreApplication.translate("MainWindow", u"Computer : 0", None))
    # retranslateUi

