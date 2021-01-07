from random import randint


class Mesaj:
    def __init__(self):
        self.header = ""
        self.message = ""
        self.token = ""
        self.packet = ""

    def set(self, packet):
        self.packet = packet

    def createPacket(self, header, mesaj):
        self.header = header
        self.message = mesaj
        self.token = randint(0, 65536)
        self.setToken(header, self.token)
        self.packet = ("" + str(header.header)).encode('UTF-8')
        if 0 < header.getTokenLength() <= 8:
            self.packet = self.packet+(str(self.token)).encode('UTF-8')
        if mesaj != "":
            self.packet = self.packet+( str(self.message)).encode('UTF-8')
        return self.packet

    def setToken(self, header, a):  #cine este a?
        if 0 < header.getTokenLength() <= 8:
            self.token = format(a, '0'+str(header.getTokenLength()*8)+'b')
    def getToken(self):
        return int(str(self.token),2)
    def getPackege(self):
        return self.packet
