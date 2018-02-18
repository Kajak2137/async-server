#! /usr/bin/env python
import asyncore, socket 
import platform
import webbrowser
from time import ctime, sleep
from getip import get_ip
host = None
port = 1488


def ipfinder(address, port):
    print "Finding Server IP, make sure you have UsoroServer running on your device!"
    getip = get_ip(address, port)
    global host
    host = unicode(getip.handle_read()) 
    return 1


class Client(asyncore.dispatcher_with_send):
    def __init__(self, host, port):
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


i = ipfinder('<broadcast>', 54545)
c = Client(host, port)
asyncore.loop()
