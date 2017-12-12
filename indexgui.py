# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'indexgui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IndexForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(301, 650)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.headicon = QtWidgets.QPushButton(Form)
        self.headicon.setMinimumSize(QtCore.QSize(51, 51))
        self.headicon.setMaximumSize(QtCore.QSize(51, 51))
        self.headicon.setObjectName("headicon")
        self.horizontalLayout.addWidget(self.headicon)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.nickname = QtWidgets.QLabel(Form)
        self.nickname.setMinimumSize(QtCore.QSize(100, 15))
        self.nickname.setObjectName("nickname")
        self.verticalLayout.addWidget(self.nickname)
        spacerItem = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.onlinelist = QtWidgets.QTreeWidget(Form)
        self.onlinelist.setMinimumSize(QtCore.QSize(281, 571))
        self.onlinelist.setObjectName("onlinelist")
        self.verticalLayout_2.addWidget(self.onlinelist)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.onlinelist.headerItem().setText(0, _translate("Form", ""))
        Form.setWindowTitle(_translate("Form", "Chat with"))
        self.headicon.setText(_translate("Form", "PushButton"))

