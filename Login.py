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
        Form.resize(450, 190)
        Form.setMinimumSize(QtCore.QSize(450, 190))
        Form.setMaximumSize(QtCore.QSize(450, 190))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 20, 81, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 150, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 101, 20))
        self.label_2.setObjectName("label_2")
        self.nickname = QtWidgets.QTextEdit(Form)
        self.nickname.setGeometry(QtCore.QRect(150, 110, 251, 31))
        self.nickname.setObjectName("nickname")
        self.iplabel = QtWidgets.QLabel(Form)
        self.iplabel.setGeometry(QtCore.QRect(150, 20, 241, 51))
        self.iplabel.setMinimumSize(QtCore.QSize(241, 51))
        self.iplabel.setObjectName("iplabel")
        self.seriplabel = QtWidgets.QLabel(Form)
        self.seriplabel.setGeometry(QtCore.QRect(50, 70, 91, 20))
        self.seriplabel.setObjectName("seriplabel")
        self.serverip = QtWidgets.QTextEdit(Form)
        self.serverip.setGeometry(QtCore.QRect(150, 70, 251, 31))
        self.serverip.setMinimumSize(QtCore.QSize(251, 31))
        self.serverip.setMaximumSize(QtCore.QSize(251, 31))
        self.serverip.setObjectName("serverip")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.nickname, self.pushButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.label.setText(_translate("Form", "本机ip地址："))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.label_2.setText(_translate("Form", "给自己起个昵称："))
        self.nickname.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:8.83019pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.83019pt;\"><br /></p></body></html>"))
        self.iplabel.setText(_translate("Form", gethostbyname(gethostname())))
        self.seriplabel.setText(_translate("Form", "服务器ip地址："))
        self.serverip.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:8.83019pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.83019pt;\"><br /></p></body></html>"))

