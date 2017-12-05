# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from socket import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(414, 150)
        Form.setMinimumSize(QtCore.QSize(414, 150))
        Form.setMaximumSize(QtCore.QSize(414, 150))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 20, 71, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 110, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 121, 16))
        self.label_2.setObjectName("label_2")
        self.nickname = QtWidgets.QTextEdit(Form)
        self.nickname.setGeometry(QtCore.QRect(150, 70, 251, 31))
        self.nickname.setObjectName("nickname")
        self.iplabel = QtWidgets.QLabel(Form)
        self.iplabel.setGeometry(QtCore.QRect(150, 20, 241, 51))
        self.iplabel.setMinimumSize(QtCore.QSize(241, 51))
        self.iplabel.setObjectName("iplabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.nickname, self.pushButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.label.setText(_translate("Form", "本机ip地址:"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.label_2.setText(_translate("Form", "顺便给自己起个昵称:"))
        self.nickname.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:8.83019pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.83019pt;\"><br /></p></body></html>"))
        ip = gethostbyname(gethostname())
        self.iplabel.setText(_translate("Form", ip))

