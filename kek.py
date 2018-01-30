
import asyncore, socket
from time import ctime
from random import randint
host = ''
port = 997
clients = []
link = raw_input("Link?: ")

class Server(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(('', port))
        self.listen(1)
        print  "Listening on port", port

    def handle_accept(self):
        # when we get a client connection start a dispatcher for that
        # client
        socket, address = self.accept()
        nickname = self.recv(1024)
        print 'Connection by', nickname
        EchoHandler(socket)


class EchoHandler(asyncore.dispatcher_with_send):
    # dispatcher_with_send extends the basic dispatcher to have an output
    # buffer that it writes whenever there's content
    def handle_read(self):

        print "going to socket"
        print nickname
        self.out_buffer = link
        print "sent"
        if not self.out_buffer:
            self.close()

s = Server(host, port)

asyncore.loop(timeout=1, count=10)

