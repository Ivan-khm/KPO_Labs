import socket
import sys

sock = socket.socket()
sock.connect(('localhost', 22))
while True:
    mes = input("Введите сообщение: ")
    if mes == 'exit':
        sock.send(mes.encode())
        sock.close()
        sys.exit()
    else:
        sock.send(mes.encode())
        print(sock.recv(1024).decode())