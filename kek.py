
import socket
from thread import *
from time import ctime

host = ''
port = 2137
clients = []
sudoers = {'root': 'toor',
           'admin': 'admin'}
kek = raw_input("Link?: ")
log = open('logs.txt', 'w')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Creating socket: OK'
log.write('Creating socket: OK \n')

try:  # Try to bind server to port
    s.bind((host, port))
except socket.error as msg:  # When something goes wrong...
    print 'Bind failed. Error Code: ' + str(msg[0]) + 'Message: ' + msg[1]
    log.write('Bind failed. Error Code: ' + str(msg[0]) + 'Message: ' + msg[1] + '\n')

print 'Binding socket: OK \n'
log.write('Binding socket: OK \n')

s.listen(0)


def kick(nickname):
    kick_info = "%s has been kicked" % nickname
    log.write("%s has been kicked \n" % nickname)
    for i in clients:
        if i[1] == nickname:
            i[0].send("You have been kicked.")
            clients.remove(i)
        i[0].send(kick_info)


def send_online_list():
    online = []
    for i in clients:
        online.append(i[1])
    online = ' '.join(online)
    online = 'Online users: ' + online
    conn.send(online)


def clientthread(conn):

    while True:
        try:
            data = conn.recv(1024)  # size of packets. In bytes.
            log.write(data+'\n')
            print data
            try:
                for i in clients:
                    if i[0] != conn:
                        i[0].send(data)
            except:
                for i in clients:
                    disc_info = str('%s has disconnected.' % (i[1]))
                    log.write(disc_info+'\n')
                    try:
                        i[0].send('')
                    except:
                        print disc_info
                        clients.remove(i)
                        conn.close()
        except:
            for i in clients:
                try:
                    i[0].send('')
                except:
                    disc_info = str('%s has disconnected.' % (i[1]))
                    log.write(disc_info+'\n')
                    print disc_info
                    clients.remove(i)
                    conn.close()

while 1:
    conn, addr = s.accept()
    conn_time = ctime()
    nc = conn.recv(1024)
    clients.append((conn, nc))
    log_info = str('\n %s %s Connected.' % (conn_time, nc))
    log.write(log_info+'\n')
    print log_info
    for i in clients:
        if i[0] != conn:
            i[0].send(log_info)
        else:
            i[0].send('System message: Praise Kek!\n' + str(kek))
    start_new_thread(clientthread, (conn,))
