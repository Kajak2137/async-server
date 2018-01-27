#GOOGLE CODE-IN COMMIT PRAISE KEK
from socket import *
import threading
from os import system
from os import name
nickname = raw_input("Nickname: ")
host = raw_input("Server: ")
port = 2137
size = 1024

system('cls' if name == 'nt' else 'clear')

s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))
s.send(nickname)


def recv_data():
    while 1:
        data = s.recv(size)
        if data:
            print data


def send_data():
    while 1:
        send = raw_input("-> ")
        send_nickname = nickname + ': ' + send
        s.send(send_nickname)

t1 = threading.Thread(target=recv_data)
t2 = threading.Thread(target=send_data)
t1.start()
t2.start()
