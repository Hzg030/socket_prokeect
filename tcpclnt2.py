from socket import *
import threading
from threading import Thread

from PyQt5.QtWidgets import QMessageBox
import sys
from PyQt5 import QtGui,QtCore,QtWidgets

class client:
    def __init__(self, serip):
        #self.conser(nickname)
        self.HOST = serip
        self.PORT = 21567
        self.BUFSIZ = 1024
        self.ADDR = (self.HOST, self.BUFSIZ)
        self.tcpclisock = socket(AF_INET, SOCK_STREAM)

    def conser(self, nickname, onlineroot, chatwindic, chatwinlis):
        try:
            self.tcpclisock.connect(self.ADDR)
        except OSError or ConnectionRefusedError:
            self.warinning()
            os._exit()
        send = 'online|' + 'nickname|' + nickname
        self.tcpclisock.send(send.encode())
        t = threading.Thread(target=self.listenline, args=(onlineroot, chatwindic, chatwinlis))
        t.start()
        t.join()

    def warinning(self):
        msg_box = QMessageBox(QMessageBox.Warning, "Alert", "无法连接到服务器!!！！", QMessageBox.Yes)
        msg_box.exec_() # 窗口停留

    def listenline(self, onlineroot, chatwindic, chatwinlist):
        while True:
            try:
                data = self.tcpclisock.recv(self.BUFSIZ)
                if data:
                    data = data.decode('utf-8')
                    mes = data.split('|')
                    if mes[0] == 'online':
                        if mes[2] == '1':
                            # 增加子根
                            self.showonline(mes[1], onlineroot)
                        elif mes[2] == '0':
                            self.delonline(mes[1], onlineroot)
                        else:
                            self.showonline(mes[1], onlineroot)
                    else:
                        mesfrom = mes[0].split(':')
                        message = mesfrom[0] + ':\n  ' + mesfrom[1]
                        for x in chatwinlist:#检查是否存在对应的聊天窗口
                            if x == mesfrom[0]:#如果存在
                                chatwindic[x].textreceive.append(message)#就在聊天窗口中显示消息
                                message = ''
                                break
                        if message:
                            for x in range(onlineroot.childCount()):#如果不存在对应的聊天窗口
                                it = onlineroot.child(x).text(0)
                                ite = it.split('|')
                                if ite[0] == mesfrom[0]:
                                    onlineroot.child(x).setText(0, it + '|  有新消息...')#就在主界面显示有新消息··
                                    t = threading.Thread(target=self.showmes, args=(mesfrom[0], message, chatwindic, chatwinlist, onlineroot.child(x), it))#并建立线程，当有该聊天窗口是在窗口中显示消息
                                    t.setDaemon(True)
                                    t.start()
            except ConnectionRefusedError or ConnectionResetError:
                self.warinning()  # 警告窗，无法链接服务器

    def showmes(self, mesfrom, message, chatwindic, chatwinlist, item, it):
        while True:
            print()
            if mesfrom in chatwinlist:
                chatwindic[mesfrom].textreceive.append(message)
                item.setText(0, it)
                return

    def delonline(self, nickname, onlineroot):
        for x in range(onlineroot.childCount()):
            it = onlineroot.child(x).text(0)
            if nickname == it:
                onlineroot.child(x).setText(0, nickname+'|不在线')
                break

    def showonline(self, nickname, onlineroot):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/head.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        for x in range(onlineroot.childCount()):#查找新新上线的人是否已存在
            it = onlineroot.child(x).text(0)
            onlineroot.child(x).serIcon(0, icon)
            ite = it.split('|')
            if nickname == ite[0]:#存在就将其状态改为在线
                onlineroot.child(x).setText(0, nickname)
                return
        item_1 = QtWidgets.QTreeWidgetItem(onlineroot)
        item_1.setIcon(0, icon)
        item_1.setText(0, nickname)

