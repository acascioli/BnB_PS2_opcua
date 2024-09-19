# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.verticalLayout = QVBoxLayout(MainPages)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.synoptic_page = QWidget()
        self.synoptic_page.setObjectName(u"synoptic_page")
        self.synoptic_page.setStyleSheet(u"font-size: 12pt")
        self.verticalLayout_7 = QVBoxLayout(self.synoptic_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_synoptic = QScrollArea(self.synoptic_page)
        self.scrollArea_synoptic.setObjectName(u"scrollArea_synoptic")
        self.scrollArea_synoptic.setFrameShape(QFrame.NoFrame)
        self.scrollArea_synoptic.setWidgetResizable(True)
        self.scrollAreaWidgetContents_synoptic = QWidget()
        self.scrollAreaWidgetContents_synoptic.setObjectName(u"scrollAreaWidgetContents_synoptic")
        self.scrollAreaWidgetContents_synoptic.setGeometry(QRect(0, 0, 842, 582))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_synoptic)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_synoptic = QLabel(self.scrollAreaWidgetContents_synoptic)
        self.label_synoptic.setObjectName(u"label_synoptic")
        self.label_synoptic.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(14)
        self.label_synoptic.setFont(font)
        self.label_synoptic.setStyleSheet(u"font-size: 14pt")
        self.label_synoptic.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_synoptic)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")

        self.horizontalLayout.addLayout(self.formLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")

        self.horizontalLayout.addLayout(self.formLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")

        self.horizontalLayout.addLayout(self.formLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")

        self.horizontalLayout.addLayout(self.formLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")

        self.horizontalLayout.addLayout(self.formLayout_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.verticalLayout_charts_synoptic = QVBoxLayout()
        self.verticalLayout_charts_synoptic.setObjectName(u"verticalLayout_charts_synoptic")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_green = QLabel(self.scrollAreaWidgetContents_synoptic)
        self.label_green.setObjectName(u"label_green")
        self.label_green.setMinimumSize(QSize(80, 20))
        self.label_green.setMaximumSize(QSize(80, 20))
        self.label_green.setStyleSheet(u"background-color: rgb(170, 255, 0);\n"
"border: 1px solid black;")

        self.horizontalLayout_3.addWidget(self.label_green)

        self.label_yellow = QLabel(self.scrollAreaWidgetContents_synoptic)
        self.label_yellow.setObjectName(u"label_yellow")
        self.label_yellow.setMinimumSize(QSize(80, 20))
        self.label_yellow.setMaximumSize(QSize(80, 20))
        self.label_yellow.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.horizontalLayout_3.addWidget(self.label_yellow)

        self.label_red = QLabel(self.scrollAreaWidgetContents_synoptic)
        self.label_red.setObjectName(u"label_red")
        self.label_red.setMinimumSize(QSize(80, 20))
        self.label_red.setMaximumSize(QSize(80, 20))
        self.label_red.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 1px solid black;")

        self.horizontalLayout_3.addWidget(self.label_red)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_synoptic)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(40, 25))
        self.label_4.setMaximumSize(QSize(40, 25))

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_plc_status = QLabel(self.scrollAreaWidgetContents_synoptic)
        self.label_plc_status.setObjectName(u"label_plc_status")
        self.label_plc_status.setMaximumSize(QSize(16777215, 25))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_plc_status.setFont(font1)
        self.label_plc_status.setStyleSheet(u"background-color: rgb(250, 250, 0);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid black;")

        self.horizontalLayout_3.addWidget(self.label_plc_status)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)


        self.verticalLayout_charts_synoptic.addLayout(self.horizontalLayout_3)


        self.verticalLayout_10.addLayout(self.verticalLayout_charts_synoptic)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")

        self.horizontalLayout_2.addLayout(self.formLayout_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")

        self.horizontalLayout_2.addLayout(self.formLayout_8)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")

        self.horizontalLayout_2.addLayout(self.formLayout_9)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName(u"formLayout_10")

        self.horizontalLayout_2.addLayout(self.formLayout_10)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.formLayout_11 = QFormLayout()
        self.formLayout_11.setObjectName(u"formLayout_11")

        self.horizontalLayout_2.addLayout(self.formLayout_11)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.formLayout_12 = QFormLayout()
        self.formLayout_12.setObjectName(u"formLayout_12")

        self.horizontalLayout_2.addLayout(self.formLayout_12)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.scrollArea_synoptic.setWidget(self.scrollAreaWidgetContents_synoptic)

        self.verticalLayout_7.addWidget(self.scrollArea_synoptic)

        self.pages.addWidget(self.synoptic_page)
        self.alerts_page = QWidget()
        self.alerts_page.setObjectName(u"alerts_page")
        self.alerts_page.setStyleSheet(u"font-size: 12pt")
        self.verticalLayout_4 = QVBoxLayout(self.alerts_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_alerts = QScrollArea(self.alerts_page)
        self.scrollArea_alerts.setObjectName(u"scrollArea_alerts")
        self.scrollArea_alerts.setFrameShape(QFrame.NoFrame)
        self.scrollArea_alerts.setWidgetResizable(True)
        self.scrollAreaWidgetContents_alerts = QWidget()
        self.scrollAreaWidgetContents_alerts.setObjectName(u"scrollAreaWidgetContents_alerts")
        self.scrollAreaWidgetContents_alerts.setGeometry(QRect(0, 0, 842, 582))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_alerts)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_alerts = QLabel(self.scrollAreaWidgetContents_alerts)
        self.label_alerts.setObjectName(u"label_alerts")
        self.label_alerts.setMaximumSize(QSize(16777215, 40))
        self.label_alerts.setFont(font)
        self.label_alerts.setStyleSheet(u"font-size: 14pt")
        self.label_alerts.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_alerts)

        self.verticalLayout_alerts = QVBoxLayout()
        self.verticalLayout_alerts.setObjectName(u"verticalLayout_alerts")

        self.verticalLayout_8.addLayout(self.verticalLayout_alerts)

        self.scrollArea_alerts.setWidget(self.scrollAreaWidgetContents_alerts)

        self.verticalLayout_4.addWidget(self.scrollArea_alerts)

        self.pages.addWidget(self.alerts_page)
        self.variables_page = QWidget()
        self.variables_page.setObjectName(u"variables_page")
        self.variables_page.setStyleSheet(u"font-size: 12pt")
        self.verticalLayout_3 = QVBoxLayout(self.variables_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_variables = QScrollArea(self.variables_page)
        self.scrollArea_variables.setObjectName(u"scrollArea_variables")
        self.scrollArea_variables.setFrameShape(QFrame.NoFrame)
        self.scrollArea_variables.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 842, 582))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_variables = QLabel(self.scrollAreaWidgetContents_2)
        self.label_variables.setObjectName(u"label_variables")
        self.label_variables.setMaximumSize(QSize(16777215, 40))
        self.label_variables.setFont(font)
        self.label_variables.setStyleSheet(u"font-size: 14pt")
        self.label_variables.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_variables)

        self.horizontalLayout_search = QHBoxLayout()
        self.horizontalLayout_search.setObjectName(u"horizontalLayout_search")

        self.verticalLayout_6.addLayout(self.horizontalLayout_search)

        self.verticalLayout_table = QVBoxLayout()
        self.verticalLayout_table.setObjectName(u"verticalLayout_table")

        self.verticalLayout_6.addLayout(self.verticalLayout_table)

        self.horizontalLayout_varCategory = QHBoxLayout()
        self.horizontalLayout_varCategory.setObjectName(u"horizontalLayout_varCategory")

        self.verticalLayout_6.addLayout(self.horizontalLayout_varCategory)

        self.scrollArea_variables.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea_variables)

        self.pages.addWidget(self.variables_page)
        self.charts_page = QWidget()
        self.charts_page.setObjectName(u"charts_page")
        self.charts_page.setStyleSheet(u"font-size: 12pt")
        self.verticalLayout_2 = QVBoxLayout(self.charts_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_charts = QScrollArea(self.charts_page)
        self.scrollArea_charts.setObjectName(u"scrollArea_charts")
        self.scrollArea_charts.setFrameShape(QFrame.NoFrame)
        self.scrollArea_charts.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 842, 582))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.label_charts = QLabel(self.scrollAreaWidgetContents)
        self.label_charts.setObjectName(u"label_charts")
        self.label_charts.setMaximumSize(QSize(16777215, 40))
        self.label_charts.setFont(font)
        self.label_charts.setStyleSheet(u"font-size: 14pt")
        self.label_charts.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_charts)

        self.verticalLayout_charts_2 = QVBoxLayout()
        self.verticalLayout_charts_2.setObjectName(u"verticalLayout_charts_2")

        self.verticalLayout_5.addLayout(self.verticalLayout_charts_2)

        self.verticalLayout_charts = QVBoxLayout()
        self.verticalLayout_charts.setObjectName(u"verticalLayout_charts")

        self.verticalLayout_5.addLayout(self.verticalLayout_charts)

        self.scrollArea_charts.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea_charts)

        self.pages.addWidget(self.charts_page)

        self.verticalLayout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label_synoptic.setText(QCoreApplication.translate("MainPages", u"Synoptic", None))
        self.label_green.setText("")
        self.label_yellow.setText("")
        self.label_red.setText("")
        self.label_4.setText("")
        self.label_plc_status.setText(QCoreApplication.translate("MainPages", u"Connecting...", None))
        self.label_alerts.setText(QCoreApplication.translate("MainPages", u"Alerts", None))
        self.label_variables.setText(QCoreApplication.translate("MainPages", u"Variables", None))
        self.label_charts.setText(QCoreApplication.translate("MainPages", u"Charts", None))
    # retranslateUi

