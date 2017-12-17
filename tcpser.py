# -*- coding: UTF-8 -*-
from socket import*
import threading
import pymysql

def handlemessage(consock, username):
    while 1:
        try:
            data = consock.recv(BUFSIZ)
        except ConnectionResetError:
            print(username, '已下线...')
            cursor = con.cursor()
            sql = """UPDATE user SET onlline = 0 WHERE nickname = '""" + username + """'"""  # 将该用户的改为不在线
            try:
                cursor.execute(sql)
                con.commit()
            except:
                con.rollback()
            cursor.close()
            condict.pop(username)
            conlist.remove(username)
            if conlist:
                telloutline(username)
            break
        if not data:
            break
        data = data.decode('utf-8')
        message = data.split('|')
        if message[0] == 'file':
            filemes = 'file|' + message[1] + '|' + message[3]
            condict[message[2]].send(filemes.encode())
        elif message[0] == 'recfile':
            recfilemes = 'recfile|' + message[1] + '|' + message[2] + '|' + message[4]
            condict[message[3]].send(recfilemes.encode())
        else:
            sendto = message[2]
            mes = message[0] + ':' + message[1]
            try:
                condict[sendto].send(mes.encode())
            except KeyError:
                sql_upload_message(message)#调用从上传消息到数据库方法

    consock.close()

def handlecon(consock):
    user = consock.recv(BUFSIZ)
    user = user.decode('utf-8')
    username = user.split('|')
    print(username[1] + "已上线...")
    if conlist:
        tellonline(username[1])#告知其他用户有人上线
    sendonline(username[1], consock)#告知该用户已在线上的人
    conlist.append(username[1])
    condict[username[1]] = consock
    sql_check_new_message(username[1])#调用从数据库检查是否有新消息方法
    handlemessage(consock, username[1])

def sql_check_new_message(username):
    cursor = con.cursor()
    sql = """Select * from user where nickname ='""" + username + """'"""  # 检查用户列表中是否存在该用户
    sqlsearch = ''
    try:
        cursor.execute(sql)
        con.commit()
        sqlsearch = cursor.fetchall()
    except:
        con.rollback()
    if sqlsearch:
        sql = """UPDATE user SET onlline = 1 WHERE nickname = '""" + username + """'"""  # 如果存在该用户就将该用户的改为在线
        try:
            cursor.execute(sql)
            con.commit()
        except:
            con.rollback()
        sql = """select fromwho ,mes from message where sendto = '""" + username + """'"""  # 查询该用户是否有未收到的消息
        messearch = ''
        try:
            cursor.execute(sql)
            con.commit()
        except:
            con.rollback()
        messearch = cursor.fetchall()
        if not messearch:  # 如果没有未收到的消息就提示没有新消息
            print(username + "没有最新消息")
        else:  # 如果有未收到的新消息，就提取消息发送并删除数据库中的记录
            for x in messearch:
                print(username + '最新消息：' + x[0] + ':' + x[1])
                mes = x[0] + ':' + x[1]
                condict[username].send(mes.encode())
            sql = """delete from message where sendto ='""" + username + """'"""
            print("数据库删除了" + username + '的最新消息')
            try:
                cursor.execute(sql)
                con.commit()
            except:
                con.rollback()
    else:  # 如果不存在该用户就在用户列表插入一条新的用户数据
        print('新用户：' + username)
        sql = """INSERT INTO user (nickname, online) VALUES ('""" + username + """', 1)"""
        try:
            cursor.execute(sql)
            con.commit()
            print('数据库新用户添加成功')
        except:
            con.rollback()
    cursor.close()

def sql_upload_message(message):#将信息保存到服务器并等待sendto再次上线
    cursor = con.cursor()
    sql = """select mes from message where sendto = '""" + message[2] +"""' and fromwho ='""" + message[0] + """'"""
    messearch = ''
    try:
        cursor.execute(sql)#查询数据库中发送给sendto的消息
        con.commit()
    except:
        con.rollback()
    messearch = cursor.fetchall()
    if not messearch:#如果没有就插入新的数据
        sql = """INSERT INTO message (fromwho, sendto, mes) VALUES ('""" + message[0] + """','""" + message[2] + """','""" + message[1] + """')"""
        try:
            cursor.execute(sql)
            con.commit()
        except:
            con.rollback()
    else:#如果有就追加更新
        sql = """update message set mes=concat(mes,'  """ + message[1] + """  ') where sendto='""" + message[2] +"""' and fromwho ='""" + message[0] + """'"""
    try:
        cursor.execute(sql)
        con.commit()
    except:
        con.rollback()
    cursor.close()

def sendonline(username, consock):
    cursor = con.cursor()
    sql = """Select * from user """  # 检查用户列表的所有用户
    sqlsearch = ''
    try:
        cursor.execute(sql)
        con.commit()
        sqlsearch = cursor.fetchall()
    except:
        con.rollback()
    cursor.close()
    for x in sqlsearch:
        if x[1] == 0 and x[0] != username:
            mes = 'online|' + x[0] + '|2'
            consock.send(mes.encode())
            mes = 'online|' + x[0] + '|0'
            consock.send(mes.encode())
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
    try:
        con = pymysql.connect(host='localhost', user='root', passwd='', db='socket', charset="utf8")#链接数据库
    except pymysql.err.OperationalError:
        print("无法链接数据库！！！！")
        exit()
    main()
