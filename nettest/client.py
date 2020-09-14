import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8841))
while True:
    cmd = input('>>:').strip()
    if not cmd:
        continue
    client.send(cmd.encode('gbk'))
    data = client.recv(1024) # 发送内容大于1024会出现粘包
    print(data.decode('gbk','ignore'))

client.close()