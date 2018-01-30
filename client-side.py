import asyncore, socket
import platform
import webbrowser


host = ''
nickname = platform.node()
port = 997

class Client(asyncore.dispatcher_with_send):
    def __init__(self, host, port, nickname):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.out_buffer = nickname

    def handle_close(self):
        self.close()

    def handle_read(self):

        self.data = self.recv(1024)
        print self.data
        webbrowser.open(self.data, new=2);
        self.close()

c = Client(host, port, nickname)
asyncore.loop(1)
       
            



