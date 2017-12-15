# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'socketGUI2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_chatWindow(object):
    def setupUi(self, chatWindow):
        chatWindow.setObjectName("chatWindow")
        chatWindow.resize(701, 688)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(chatWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.headbutton = QtWidgets.QPushButton(chatWindow)
        self.headbutton.setMinimumSize(QtCore.QSize(61, 61))
        self.headbutton.setMaximumSize(QtCore.QSize(61, 61))

        self.headbutton.setObjectName("headbutton")
        self.horizontalLayout_3.addWidget(self.headbutton)
        self.namelabel = QtWidgets.QLabel(chatWindow)
        self.namelabel.setMinimumSize(QtCore.QSize(63, 21))
        self.namelabel.setMaximumSize(QtCore.QSize(63, 21))
        self.namelabel.setObjectName("namelabel")
        self.horizontalLayout_3.addWidget(self.namelabel)
        spacerItem = QtWidgets.QSpacerItem(538, 48, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textreceive = QtWidgets.QTextBrowser(chatWindow)
        self.textreceive.setMinimumSize(QtCore.QSize(681, 400))
        self.textreceive.setObjectName("textreceive")
        self.verticalLayout.addWidget(self.textreceive)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.emojibutton = QtWidgets.QPushButton(chatWindow)
        self.emojibutton.setMinimumSize(QtCore.QSize(25, 25))
        self.emojibutton.setMaximumSize(QtCore.QSize(25, 25))
        self.emojibutton.setObjectName("emojibutton")
        self.horizontalLayout_2.addWidget(self.emojibutton)
        self.filebutton = QtWidgets.QPushButton(chatWindow)
        self.filebutton.setMinimumSize(QtCore.QSize(25, 25))
        self.filebutton.setMaximumSize(QtCore.QSize(25, 25))
        self.filebutton.setObjectName("filebutton")
        self.horizontalLayout_2.addWidget(self.filebutton)
        spacerItem1 = QtWidgets.QSpacerItem(608, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textsent = QtWidgets.QTextEdit(chatWindow)
        self.textsent.setMinimumSize(QtCore.QSize(681, 100))
        self.textsent.setMaximumSize(QtCore.QSize(16777215, 130))
        self.textsent.setObjectName("textsent")
        self.verticalLayout.addWidget(self.textsent)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(578, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.sentbutton = QtWidgets.QPushButton(chatWindow)
        self.sentbutton.setMinimumSize(QtCore.QSize(82, 31))
        self.sentbutton.setMaximumSize(QtCore.QSize(82, 31))
        self.sentbutton.setObjectName("sentbutton")
        self.horizontalLayout.addWidget(self.sentbutton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.headbutton.setStyleSheet("border-image: url(img/head.png);")
        self.emojibutton.setStyleSheet("border-image: url(img/emoji.ico);")
        self.filebutton.setStyleSheet("border-image: url(img/file.png);")

        self.retranslateUi(chatWindow)
        QtCore.QMetaObject.connectSlotsByName(chatWindow)

    def retranslateUi(self, chatWindow):
        _translate = QtCore.QCoreApplication.translate
        chatWindow.setWindowTitle(_translate("chatWindow", "Chat"))
        self.sentbutton.setText(_translate("chatWindow", "发送"))

