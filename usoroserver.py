import asyncore, socket, webbrowser
host = ''
port = 1488
nickname  = 'TestKajak'

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
        data = raw_input('Enter link to send: ')
        self.send(data)
        if not self.send:
            self.close()

s = Server(host, port)
asyncore.loop()

