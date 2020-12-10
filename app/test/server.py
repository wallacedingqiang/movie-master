'''
created on April 5 2019 20:32
filename: server.py
@author: lhy
'''
#服务器端
import socket
import threading


#接受客户端消息函数
def recv_msg(clientsocket):
    while True:
        # 接受客户端消息,设置一次最多接受1024字节的数据
        recv_msg = clientsocket.recv(1024)
        # 把接收到的东西解码
        msg = recv_msg.decode('utf-8')
        # 如果用户输入了quit，就退出此对话
        if msg == 'quit':
            exit(0)
        print('Win10 say: ' + msg)

def main():
    #创建服务器端socket对象 ipv4 + TCP协议，和客户端一样
    socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 注意注意注意，我们要绑定监听的地址和端口。服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上，也可以用0.0.0.0绑定到所有的网络地址
    # 还可以用127.0.0.1绑定到本机地址。127.0.0.1是一个特殊的IP地址，表示本机地址，如果绑定到这个地址，客户端必须同时在本机运行才能连接，也就是说，外部的计算机无法连接进来。
    # 这个程序中host使用'0.0.0.0'或服务器内网ip地址都可以，我这里就使用了内网ip地址
    #host='0.0.0.0'
    host='10.206.0.4'
    #设置被监听的端口号,小于1024的端口号不能使用，因为他们是Internet标准服务的端口号
    port=1234

    #绑定地址
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind((host,port))
    #设置最大监听数，也就是最多可以同时响应几个客户端请求，一般配合多线程使用
    socket_server.listen(5)
    #等待客户端连接,一旦有了连接就立刻向下执行，否则等待
    #accept()函数会返回一个元组，第一个元素是客户端socket对象，第二个元素是客户端地址（ip地址+端口号）
    clientsocket,addr=socket_server.accept()

    # 有了客户端连接后之后才能执行以下代码，我们先向客户端发送连接成功消息
    clientsocket.send('你现在已经连接上了服务器啦，我们来聊天吧！'.encode('utf-8'))

    # 和客户端一样开启一个线程接受客户端的信息
    t=threading.Thread(target=recv_msg,args=(clientsocket,))
    t.start()


    # 发送消息
    while True:
        reply=input()
        clientsocket.send(reply.encode('utf-8'))

    clientsocket.close()


if __name__=='__main__':
    main()
