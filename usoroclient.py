#! /usr/bin/env python
import asyncore, socket
import webbrowser
from time import ctime, sleep
from getip import GetIP
host = None
port = 1488


def ipfinder():
    print "Finding Server IP, make sure you have UsoroServer running on your device!"
    ip = GetIP()
    global host
    host = unicode(ip.handle_read())
    return 1


class Client(asyncore.dispatcher_with_send):
    def __init__(self):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.out_buffer = 'kajak'

    def handle_close(self):
        print "Closing"
        self.close()

    def handle_read(self):
        while 1:
            try: 
                data = self.recv(1024)
                if data:
                    webbrowser.open(data, new=2)
            except socket.error:
                    if str(socket.error) == "[Errno 35] Resource temporarily unavailable":
                        sleep(0)
                        continue


i = ipfinder()
c = Client()
asyncore.loop()
