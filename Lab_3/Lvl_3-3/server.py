import random
import socket


def rand_son():
    spis = ["Hi", "Hello", "Salut", "Bye", "Hallo", "Hola", "Oi"]
    rand_spis = random.choice(spis)
    return rand_spis


sock = socket.socket()
sock.bind(('', 22))
sock.listen(15)
connect, addr = sock.accept()

while True:
    data = connect.recv(1024)
    if not data:
        break
    else:
        sonnet = rand_son()
        connect.send(sonnet.encode())
connect.close()
