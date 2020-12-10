'''
created on April 5 2019 20:23
filename: client.py
@author: lhy
'''
#客户端代码
import socket
import threading

#接受服务器返回的数据的函数
def recvlink(client):
    while True:
        msg=client.recv(1024)
        print('Ubuntu say: '+msg.decode('utf-8'))

def main():
    #创建ipv4的socket对象，使用TCP协议(SOCK_STREAM)
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #设置服务器ip地址，注意应该是服务器的公网ip
    host='119.45.202.96'
    #设置要发送到的服务器端口,需要在云服务器管理界面打开对应端口的防火墙
    port=1234

    #建立TCP协议连接,这时候服务器就会监听到到连接请求，并开始等待接受client发送的数据
    client.connect((host,port))

    #建立连接后，服务器端会返回连接成功消息
    start_msg=client.recv(1024)
    print(start_msg.decode('utf-8'))

    #开启一个线程用来接受服务器发来的消息
    t=threading.Thread(target=recvlink,args=(client,))
    t.start()

    #发送消息
    while True:
        #输入要发送的信息
        sendmsg=input()
        #向服务器发送消息
        client.send(sendmsg.encode('utf-8'))
        if sendmsg=='quit':
            break
    #结束时关闭客户端
    client.close()

if __name__ == '__main__':
    main()

