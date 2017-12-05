from socket import *
import threading


def sendmessage(tcpclisock, nickname, sendto):
    while True:
        data = input('> ')
        if not data:
            break
        data = nickname + ':' + data + '|' + sendto
        tcpclisock.send(data.encode())

def recmessage(tcpclisock):
    while True:
        data = tcpclisock.recv(BUFSIZ)
        if not data:
            break
        print(data.decode('utf-8'))

def conser(nickname):
    try:
        tcpclisock.connect(ADDR)
    except ConnectionRefusedError:
        warinning()
    send = 'nickname|' + nickname
    tcpclisock.send(send.encode())
    t = threading.Thread(target=listenline)
    t.start()
    t.join()

def warinning():
    print('无法连接到服务器!!')
    pass#警告窗口：无法连接服务器

def listenline():
    while True:
        try:
            data = tcpclisock.recv(BUFSIZ)
            if data:
                data = data.decode('utf-8')
                mes = data.split('|')
                if mes[1] == '1':
                    #增加子根
                    showonline(mes[0])
                elif mes[1] == '0':
                    delonline(mes[0])
                else:
                    showonline(mes[0])
        except ConnectionRefusedError:
            warinning()#警告窗，无法链接服务器

def delonline(nickname):
    print(nickname + '下线了')
    pass#删除在线列表中下线的人

def showonline(nickname):
    print(nickname + '上线了')
    pass#在在线列表中增加子根

def connectto(nickname, sendto):
    t1 = threading.Thread(target=sendmessage, args=(tcpclisock, nickname, sendto))
    t2 = threading.Thread(target=recmessage, args=(tcpclisock,))
    t = []
    t.append(t1)
    t.append(t2)
    for x in t:
        x.setDaemon(True)
        x.start()
    x.join()
    tcpclisock.close()

def main(nickname):
    conser(nickname)
    #if pushbutton:
       # connectto(nickname, sendto)

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, BUFSIZ)
    tcpclisock = socket(AF_INET, SOCK_STREAM)
    main('hzg003')