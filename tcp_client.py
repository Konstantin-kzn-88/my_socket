import socket


def recvall(sock):
    BUFF_SIZE = 4096 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            break
    return data


var = 91000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8888))
msg = str([i*i for i in range(var)]).encode()
sock.send(msg)
res = recvall(sock)
ans = res.decode()
print(len(ans), ans)
sock.close()