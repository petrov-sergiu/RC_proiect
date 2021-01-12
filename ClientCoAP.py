from CoAP import Coap
import threading

class Client(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.coap = Coap()
        self.coap.start()
        self.ip = '0.0.0.0'
        self.port = 4321
        self.message = ""

    def run(self):
        self.coap.get(self.ip, self.port, 'MESAJ')
        self.message = self.coap.getResult()

    def returnMessage(self):
        return self.message


