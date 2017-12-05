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
        sendto = message[1]
        print(message[0])
        condict[sendto].send(message[0].encode())
    consock.close()

def handlecon(consock):
    user = consock.recv(BUFSIZ)
    user = user.decode('utf-8')
    username = user.split('|')
    if conlist:
        tellonline(username[1])
        sendonline(consock)
    conlist.append(username[1])
    condict[username[1]] = consock

    print(username[1], '已上线...')
    handlemessage(consock, username[1])

def sendonline(consock):
    for x in conlist:
            mes = x + '|2'
            consock.send(mes.encode())

def telloutline(nickname):
    for x in conlist:
            mes = nickname+'|0'
            condict[x].send(mes.encode())

def tellonline(nickname):
    for x in conlist:
            mes = nickname + '|1'
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