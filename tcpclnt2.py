# -*- coding:utf8 -*-
#encoding = utf-8
from socket import *
import threading
from threading import Thread
from PyQt5.QtWidgets import QMessageBox
import sys
from PyQt5 import QtGui,QtCore,QtWidgets
import struct
from filesendGui import Ui_FileForm
import os

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
            exit()
        send = 'online|' + nickname
        self.tcpclisock.send(send.encode())
        t = threading.Thread(target=self.listenline, args=(onlineroot, chatwindic, chatwinlis))
        t.start()
        t.join()

    def warinning(self):
        self.msg_box = QMessageBox(QMessageBox.Warning, "无法链接服务器！", "无法连接到服务器!!！！", QMessageBox.Yes)
        self.msg_box.exec_() # 窗口停留

    def listenline(self, onlineroot, chatwindic, chatwinlist):#监听消息函数
        while True:
            try:
                data = self.tcpclisock.recv(self.BUFSIZ)
                if data:
                    data = data.decode('utf-8')
                    mes = data.split('|')
                    if mes[0] == 'online':#如果消息头为online，则表明这是一个上线消息，在主界面中增加上线好友
                        self.tellonline(mes[2], mes[1], onlineroot)
                    elif mes[0] == 'file':#如果消息头为file表示为文件消息
                        filesercon = socket(AF_INET, SOCK_STREAM)#用一个新的端口建立服务器来准备接受文件
                        host = gethostbyname(gethostname())
                        serport = 12345
                        addr = 'recfile|' + host + '|' + str(serport) + '|' + mes[1] + '|' + mes[2]
                        self.tcpclisock.send(addr.encode())  # 把ip发送给服务器，等待接收文件
                        filesercon.bind((host, serport))
                        filesercon.listen(5)
                        t = threading.Thread(target=self.fileser, args=(filesercon, ))#建立服务器线程
                        t.start()
                    elif mes[0] == 'recfile':#如果消息头为recfile，表示对方已准备好接受文件，此时发送文件
                        t = threading.Thread(target=self.sendfile, args=(mes[1], int(mes[2]), mes[3]))
                        t.start()
                    else:#如果以上都不是则为普通消息
                        self.check_chatwin(mes, chatwinlist, chatwindic, onlineroot)
            except ConnectionRefusedError or ConnectionResetError:
                self.warinning()  # 警告窗，无法链接服务器

    def sendfile(self, host, addr, filename):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((host, addr))
        FILEINFO_SIZE = struct.calcsize('128sI')  #编码格式大小
        fhead = struct.pack('128sI', filename.encode(), os.stat(filename).st_size)
        print('文件打包')# 按照规则进行打包
        fp = open(filename, 'rb')
        sock.send(fhead)  # 发送文件基本信息数据
        filesize = os.stat(filename).st_size
        while 1:  # 发送文件
            filedata = fp.read(self.BUFSIZ)
            if not filedata:
                break
            sock.send(filedata)
            filesize = filesize - len(filedata)
        print("sending over...")
        fp.close()

    def fileser(self, filesercon):
        filecon, fileaddr = filesercon.accept()
        FILEINFO_SIZE = struct.calcsize('128sI')
        '''''定义文件信息（包含文件名和文件大小）大小。128s代表128个char[]（文件名），I代表一个integer or long（文件大小）'''
        while 1:
            try:
                fhead = filecon.recv(FILEINFO_SIZE)
                filename, filesize = struct.unpack('128sI', fhead) #把接收到的数据包按照打包规则128sI进行解包
                filename = filename.decode().strip('\00')  #去除数据中的\00
                filename = filename.split('/')[-1]
                fp = open(filename, 'wb')  # 新建文件，并且准备写入
                restsize = filesize
                print("recving...")
                while 1:
                    if restsize > self.BUFSIZ:  # 如果剩余数据包大于1024，就取1024的数据包
                        try:
                            filedata = filecon.recv(self.BUFSIZ)
                        except ConnectionResetError:
                            self.msg_box = QMessageBox(QMessageBox.Warning, "失去连接！！", "与对方失去连接！！！", QMessageBox.Yes)
                            self.msg_box.show()
                    else:
                        filedata = filecon.recv(restsize)
                        fp.write(filedata)
                        break
                    if not filedata:
                        break
                    fp.write(filedata)
                    restsize = restsize - len(filedata)  # 计算剩余数据包大小
                    if restsize <= 0:
                        break
                fp.close()
                print("recv succeeded !!File named:", filename)
                filecon.close()
                #filesercon.close()
                break
            except struct.error:
                break

    def tellonline(self, typenum, nickname, onlineroot):
        if typenum == '1':
            # 增加子根
            self.showonline(nickname, onlineroot)
        elif typenum == '0':
            self.delonline(nickname, onlineroot)
        else:
            self.showonline(nickname, onlineroot)

    def check_chatwin(self, mes, chatwinlist, chatwindic, onlineroot, ):
        mesfrom = mes[0].split(':')
        message = mesfrom[0] + ':\n  ' + mesfrom[1]
        for x in chatwinlist:  # 检查是否存在对应的聊天窗口
            if x == mesfrom[0]:  # 如果存在
                chatwindic[x].textreceive.append(message)  # 就在聊天窗口中显示消息
                message = ''
                break
        if message:
            for x in range(onlineroot.childCount()):  # 如果不存在对应的聊天窗口
                it = onlineroot.child(x).text(0)
                ite = it.split('|')
                if ite[0] == mesfrom[0]:
                    onlineroot.child(x).setText(0, it + '|  有新消息...')  # 就在主界面显示有新消息··
                    t = threading.Thread(target=self.showmes, args=(
                    mesfrom[0], message, chatwindic, chatwinlist, onlineroot.child(x), it))  # 并建立线程，当有该聊天窗口是在窗口中显示消息
                    t.setDaemon(True)
                    t.start()

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
            onlineroot.child(x).setIcon(0, icon)
            ite = it.split('|')
            if nickname == ite[0]:#存在就将其状态改为在线
                onlineroot.child(x).setText(0, nickname)
                return
        item_1 = QtWidgets.QTreeWidgetItem(onlineroot)
        item_1.setIcon(0, icon)
        item_1.setText(0, nickname)


class filewindow(QtWidgets.QWidget, Ui_FileForm):
    def __init__(self):
        super(filewindow, self).__init__()
        self.setupUi(self)
