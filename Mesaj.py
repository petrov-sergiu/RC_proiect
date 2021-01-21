from random import randint


class Mesaj:
    def __init__(self):
        self.packet = ""

    def setPack(self, packet):
        self.packet = packet

    def createPacket(self, header, message):
        self.packet = ("" + str(header.getHeader())).encode('UTF-8')
        if 0 < header.getTokenLength() <= 8:
            header.setToken(randint(0, pow(2, header.getTokenLength())))
            self.packet = self.packet + (str(header.token)).encode('UTF-8')
        if message != "":
            self.packet = self.packet+(str(message)).encode('UTF-8')
        return self.packet
##############///////////////////
    def despachetarePacket(self):
        despachetare=self.packet.decode('UTF-8')
        tokenLen=4
        self.header=despachetare[0:32+tokenLen*8]
        self.message=despachetare[32+tokenLen*8]
        return(self.header, self.message)


    def getPackege(self):
        return self.packet
