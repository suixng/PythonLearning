from socket import socket,SOCK_STREAM,AF_INET
from datetime import datetime

def main():
    #1.创建套接字对象并指定使用哪种传输服务
    #2.family=AF_INET   IPv4地址
    #3.family=AF_INEt6  IPv6地址
    #4.type=SOCK_STREAM  TCP套接字
    #5.type=SOCK_DGRAM  UDP套接字
    #6.type=SOCK_RAW    原始套接字
    server = socket(family=AF_INET,type=SOCK_STREAM)
    #2.绑定IP地址和端口（端口用于区分不同服务）
    #同一时间只能在一个端口号上绑定一个服务否则报错
    server.bind(('127.0.0.1',8841))
    #3.开始监听——监听客户端连接到服务器
    #参数512可以理解我链接队列的大小
    server.listen(512)
    print('服务器启动开始监听')
    while True:
        #4.通过循环接受客户端的连接并作出相应处理（提供服务）
        #accept()方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        #accept()方法返回第一个元组其中的第一个元素是服务器对象
        #第二个元素是连接到服务器的客户端的地址（由IP和端口号两部分构成）
        client,addr = server.accept()
        print(str(addr) + '连接到了服务器')
        #5.发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        #6.断开连接
        client.close()

if __name__ == '__main__':
    main()
