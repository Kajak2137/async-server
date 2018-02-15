import asyncore, socket, webbrowser
from time import ctime, sleep
from random import randint
host = ''
port = 1488
clients = []

class Server(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        print  "Listening on port", port
        self.bind(('', port))
        self.listen(5)

    def handle_accept(self):
        # when we get a client connection start a dispatcher for that
        # client
        socket, address = self.accept()
        print 'Connection by', address
        EchoHandler(socket)

class EchoHandler(asyncore.dispatcher_with_send):
    # dispatcher_with_send extends the basic dispatcher to have an output
    # buffer that it writes whenever there's content

    def handle_read(self):
        link = raw_input('Enter Link: ')
        self.out_buffer = link
        print self.out_buffer
        if not self.out_buffer:
            self.close()

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

s = Server(host, port)
c = Client(host, port)
asyncore.loop()

