import asyncore, socket
import platform
import webbrowser
from time import ctime, sleep

host = ''
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
      #  while 1:
      #         sleep(1)
      #         self.x = data
      #          if data is self.x:
      #          	print "Nothing changed"
      #          else: 
      #          	print "data changed"
    
   # def handle_open(self):
   #     self.x = data
   #     while data is self.x:
    #        webbrowser.open(data, new=2);
    #        print "Browser Opened"
   #         break
   #     else:
    #       print "link changed"
    #       webbrowser.open(data, new=2); 
                
c = Client(host, port)
asyncore.loop()