# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setMaximumSize(QSize(400, 300))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 90, 161, 91))
        font = QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_time = QLabel(Form)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setGeometry(QRect(130, 210, 141, 21))
        self.label_time.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u53bb\u559d\u6c34", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u53bb\u559d\u6c34", None))
        self.label_time.setText(QCoreApplication.translate("Form", u"time", None))
    # retranslateUi

