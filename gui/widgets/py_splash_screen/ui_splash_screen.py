# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #2c313c;\n"
"	color: rgb(220, 220, 220);\n"
"border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 80, 661, 71))
        font = QFont()
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setLayoutDirection(Qt.LeftToRight)
        self.label_title.setStyleSheet(u"color: #568af2;")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(-4, 150, 661, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setLayoutDirection(Qt.LeftToRight)
        self.label_description.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 260, 561, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.517, x2:1, y2:0.551, stop:0 rgba(86, 138, 242, 255), stop:1 rgba(59, 95, 166, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 300, 661, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_loading.setFont(font2)
        self.label_loading.setLayoutDirection(Qt.LeftToRight)
        self.label_loading.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(20, 340, 621, 31))
        font3 = QFont()
        font3.setPointSize(10)
        self.label_credits.setFont(font3)
        self.label_credits.setLayoutDirection(Qt.LeftToRight)
        self.label_credits.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<strong>HTL</strong> BnBLab", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"<strong>GUI</strong> Hydrothermal Liquefaction", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen", u"<strong>Created</strong> by AC", None))
    # retranslateUi

