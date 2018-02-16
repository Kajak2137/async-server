#! /usr/bin/env python
import asyncore, socket 
import platform
import webbrowser
from time import ctime, sleep

host = raw_input("What's the IP address of your PC?: ")
# nickname = platform.node()
port = 1488

class Client(asyncore.dispatcher_with_send):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.out_buffer = 'kajak'

    def handle_close(self):
        self.close()
        print 'Going Offline'

    def handle_read(self):
        while 1:
            try: 
                data = self.recv(1024)
                if data:
                	webbrowser.open(data, new=2);
            except socket.error:
                    if str(socket.error) == "[Errno 35] Resource temporarily unavailable":
                        time.sleep(0)
                        continue                   
c = Client(host, port)
asyncore.loop()
