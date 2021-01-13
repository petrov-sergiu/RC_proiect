from random import randint


class Mesaj:
    def __init__(self):
        self.header = ""
        self.message = ""
        self.token = ""
        self.packet = ""

    def set(self, packet):
        self.packet = packet

    def createPacket(self, header, mesasage):
        self.header = header
        self.message = mesasage
        self.token = randint(0, 65536)
        self.packet = ("" + str(header.header)).encode('UTF-8')
        if 0 < header.getTokenLength() <= 8:
            self.packet = self.packet+(str(self.token)).encode('UTF-8')
        if mesasage != "":
            self.packet = self.packet+(str(self.message)).encode('UTF-8')
        return self.packet

    def despachetarePacket(self):
        despachetare=self.packet.decode('UTF-8')
        tokenLen=4
        self.header=despachetare[0:32+tokenLen*8]
        self.message=despachetare[32+tokenLen*8]
        return(self.header, self.message)


    def getPackege(self):
        return self.packet
