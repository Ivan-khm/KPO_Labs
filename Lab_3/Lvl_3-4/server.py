import random
import socket


def open_file():
    try:
        file = open('Shakespeare.txt', 'r')
        list_sonnets = file.read().split('+')
        print(list_sonnets)
        file.close()
        return list_sonnets
    except:
        print("Ошибка!")


def rand_son():
    op = open_file()
    random_sonnets = random.choice(op)
    return random_sonnets


sock = socket.socket()
sock.bind(('', 8888))
sock.listen(15)
connect, addr = sock.accept()

print('Подключен:', addr)

while True:
    data = connect.recv(1024)
    if not data:
        break
    else:
        sonnet = rand_son()
        connect.send(sonnet.encode())
connect.close()
 
