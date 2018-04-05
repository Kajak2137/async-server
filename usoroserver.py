#! /usr/bin/env python
import asyncore, socket
from getip import BroadcastIP
port = 1488


class Server(asyncore.dispatcher):
    def __init__(self):
        asyncore.dispatcher.__init__(self)
        broadcaster()
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        print "Please open UsoroClient on your second device"
        print "Waiting for Connection"
        self.bind(('', port))
        self.listen(5)

    def handle_accept(self):
        # when we get a client connection start a dispatcher for that
        # client
        sock, addr = self.accept()
        print 'Connection by', addr
        EchoHandler(socket)


def broadcaster():
    BroadcastIP()


class EchoHandler(asyncore.dispatcher_with_send):
    # dispatcher_with_send extends the basic dispatcher to have an output
    # buffer that it writes whenever there's content

    def handle_read(self):
        data = raw_input('Enter link to send: ')
        self.send(data)
        if not self.send:
            self.close()


s = Server()
asyncore.loop()
