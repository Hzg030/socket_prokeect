from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Login import Ui_Form
from indexgui import Ui_IndexForm
from socketGUI2 import Ui_chatWindow
import sys
from tcpclnt2 import *
import threading
#from socket import *
#import threading

class indexwindow(QtWidgets.QWidget,Ui_IndexForm):#登陆后主界面
    def __init__(self):
        super(indexwindow, self).__init__()
        self.setupUi(self)
        onlineroot = QtWidgets.QTreeWidgetItem(self.onlinelist)
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.onlinelist.isSortingEnabled()
        self.onlinelist.setSortingEnabled(False)
        self.onlinelist.topLevelItem(0).setText(0, _translate("Form", "好友列表"))
        self.onlinelist.setSortingEnabled(__sortingEnabled)
        self.onlinelist.itemDoubleClicked.connect(self.chat)#双击在线好友事件
        self.chatwindic = dict()
        self.chatwinlist = list()

    def closeEvent(self, event):#关闭主界面窗口时断开与服务器的连接
        reply = QMessageBox(QMessageBox.Warning)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def chat(self, item):#双击在线好友时打开聊天窗口
        it = item.text(0)
        sendto = it.split('|')[0]
        if sendto != '好友列表':
            self.chatwin = chatwindow(sendto)
            self.chatwinlist.append(sendto)
            self.chatwindic[sendto] = self.chatwin
            self.chatwin.show()
            self.chatwin.namelabel.setText(sendto)

    def hanleclick(self, nickname):
        self.nickname = nickname
        if not self.isVisible():
            self.show()

class chatwindow(QtWidgets.QWidget,Ui_chatWindow):#聊天窗口类
    def __init__(self, sendto):
        super(chatwindow, self).__init__()
        self.setupUi(self)
        self.sendto = sendto
        self.nickname = loginwin.idewindow.nickname
        self.sentbutton.clicked.connect(self.sendmessage)
        self.filebutton.clicked.connect(self.choosefile)

    def closeEvent(self, event):
        loginwin.idewindow.chatwinlist.remove(self.sendto)
        loginwin.idewindow.chatwindic.pop(self.sendto)

    def sendmessage(self):#发送信息
        s = self.textsent.toPlainText()
        strin = str(s)
        if strin:
            self.textreceive.append(loginwin.nickname_ + ':\n  ' + strin)
            strin = loginwin.nickname_ + '|' + strin + '|' + self.sendto
            loginwin.clnt.tcpclisock.send(strin.encode())
            strin = ''
        self.textsent.clear()

    def choosefile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "选择文件", "C:\\Users\Administrator\Desktop", '*')
        if filename:
            filemes = "file|" + self.nickname + '|' + self.sendto + '|' + filename[0]
            loginwin.clnt.tcpclisock.send(filemes.encode())

class loginwindow(QtWidgets.QWidget,Ui_Form):#登陆窗口类
    def __init__(self):
        super(loginwindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ifpushbutton)

    def ifpushbutton(self):#点击确认按钮函数
        self.nickname_ = self.nickname.toPlainText()
        serip = self.serverip.toPlainText()
        if not serip:
            msg_box = QMessageBox(QMessageBox.Warning, "Alert", "服务器ip不能为空！！", QMessageBox.Yes)
            msg_box.exec_()  # 窗口停留
        elif not self.nickname_:
            msg_box = QMessageBox(QMessageBox.Warning, "Alert", "昵称不能为空！！", QMessageBox.Yes)
            msg_box.exec_()#窗口停留
        else:
            self.showindex(self.nickname_, serip)

    def showindex(self, nickname, serip):#显示主界面窗口
        self.idewindow = indexwindow()
        _translate = QtCore.QCoreApplication.translate
        self.idewindow.nickname.setText(_translate("Form", nickname))
        self.idewindow.hanleclick(nickname)
        self.close()
        t = threading.Thread(target=self.connect, args=(nickname, serip))
        t.start()

    def connect(self, nickname, serip):#声明客户端对象，并连接到服务器，监听上线信息
        self.clnt = client(serip)
        self.clnt.conser(nickname, self.idewindow.onlinelist.topLevelItem(0), self.idewindow.chatwindic, self.idewindow.chatwinlist)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loginwin = loginwindow()
    loginwin.show()
    sys.exit(app.exec_())
