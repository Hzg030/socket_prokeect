from socket import*
import threading

def handlemessage(consock, username):
    while 1:
        try:
            data = consock.recv(BUFSIZ)
        except ConnectionResetError:
            print(username, '已下线...')
            condict.pop(username)
            conlist.remove(username)
            if conlist:
                telloutline(username)
            break
        if not data:
            break
        data = data.decode('utf-8')
        message = data.split('|')
        sendto = message[2]
        mes = message[0] + ':' + message[1]
        print(mes)
        try:
            condict[sendto].send(mes.encode())
        except KeyError:
            pass#将信息保存到服务器并等待sendto再次上线
    consock.close()

def handlecon(consock):
    user = consock.recv(BUFSIZ)
    user = user.decode('utf-8')
    username = user.split('|')
    if conlist:
        tellonline(username[2])
        sendonline(consock)
    conlist.append(username[2])
    condict[username[2]] = consock
    print(username[2], '已上线...')
    handlemessage(consock, username[2])


def sendonline(consock):
    for x in conlist:
            mes = 'online|' + x + '|2'
            consock.send(mes.encode())

def telloutline(nickname):
    for x in conlist:
            mes = 'online|' + nickname+'|0'
            condict[x].send(mes.encode())

def tellonline(nickname):
    for x in conlist:
            mes = 'online|' + nickname + '|1'
            condict[x].send(mes.encode())

def main():
    tcpsersock = socket(AF_INET, SOCK_STREAM)
    tcpsersock.bind(ADDR)
    tcpsersock.listen(5)
    print('服务器已启动。。。')

    while True:
        tcpclisock, addr = tcpsersock.accept()
        t = threading.Thread(target=handlecon, args=(tcpclisock,))
        t.start()

if __name__ == '__main__':
    HOST = ''
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, BUFSIZ)
    condict = dict()
    conlist = list()
    main()
