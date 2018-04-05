import Queue
import asyncore, socket

host = '<broadcast>'
port = 54545
data = "Request"


class GetIP(asyncore.dispatcher):
    def __init__(self):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sendto(data, ('<broadcast>', 54545))

    def handle_read(self):
        while 1:
            try:
                recv_data, addr = self.recvfrom(1500)
                ip = addr[0]
                return ip
                self.handle_close()
            except socket.error:
                if str(socket.error) == "[Errno 35] Resource temporarily unavailable":
                    time.sleep(0)
                    continue

    def writable(self):
        return False

    def handle_close(self):
        asyncore.dispatcher.close(self)
        print "Closing"
        self.close()


class BroadcastIP(asyncore.dispatcher):
    def __init__(self):
        asyncore.dispatcher.__init__(self)
        self.callback = None
        self.port = port
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.send_queue = Queue.Queue()

    def handle_connect(self):
        pass

    def handle_read(self):
        recv_data, addr = self.recvfrom(1500)
        self.sendto("*" + recv_data, addr)
        self.handle_close()

    def handle_close(self):
        asyncore.dispatcher.close(self)
        print "Closing"
        self.close()
