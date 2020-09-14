import socket
import subprocess  # 允许我们启动一个新进程，并连接到它们的输入/输出/管道，从而获取返回值。
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8841))
server.listen(5)
while True:
    conn, client = server.accept()
    while True:
        try:
            # 收命令
            cmd = conn.recv(1024)

            # 执行命令、拿到结果
            obj = subprocess.Popen(cmd.decode('gbk'), shell=True,
                                   stdout=subprocess.PIPE,  # 存放命令正确得到结果的通道
                                   stderr=subprocess.PIPE)  # 存放命令错误得到结果的通道
            stdout = obj.stdout.read()  # 把里面的内容读出来放在这里
            stdeer = obj.stderr.read()

            conn.send(stdout+stdeer) 
        except ConnectionResetError as err:
            break
    conn.close()
server.close()
