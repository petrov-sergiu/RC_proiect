class Header:
    def __init__(self):
        self.header = None
        # version= 01 "mereu"
        self.version = 0
        # tipul mesajului: Confirmabil 00/ Neconfirmabil 01/ Acknowledg 10/ Reset 11
        self.type = 0
        # Indica lungimea var Token
        self.tokenLength = 0
        # Primii 3 bit din cod
        self.codeClass = 0
        #  Ceilalti 5 bit din cod
        self.codeDetail = 0
        # 16 bit
        self.messageId = 0

        self.code = None

    def setHeader(self, version, typ, tokenL):
        self.version = format(version, '02b')
        self.type = format(typ, '02b')
        self.tokenLength = format(tokenL, '04b')
        self.header = (version << 6) + (typ << 4) + tokenL
        self.header = format(self.header, '08b')

    def setCode(self, clas, detail):
        self.codeClass = format(clas, '03b')
        self.codeDetail = format(detail, '05b')
        self.code = (clas << 5) + detail
        self.code = format(self.code, '08b')

    def setMessageId(self, a):
        self.messageId = format(a, '016b')


    def getTokenLength(self) -> int:
        return int(str(self.tokenLength), 2)

    def buildHeader(self) -> str:
        self.header = "" + str(self.header) + str(self.code) + str(self.messageId)
        return self.header

    def print(self):
        print("\n\nHeaderul-> ")
        print("Version= " + str(self.getVersion()))
        print("Message Type= " + str(self.getMessageType()))
        print("Token Length=" + str(self.getTokenLength()))
        print("CodeClass= " + str(self.getCodeClass()))
        print("CodeDetail= " + str(self.getCodeDetail()))
        print("MessageId=" + str(self.getMessageId()))
        print("Headerul-> " + str(self.header))
        print("Header size->" + str(len(self.header)))

    def getVersion(self):
        return int(str(self.version), 2)

    def getMessageType(self):
        return int(str(self.type), 2)

    def getCodeClass(self):
        return int(str(self.codeClass), 2)

    def getCodeDetail(self):
        return int(str(self.codeDetail), 2)

    def getCode(self):
        return int(str(self.code), 2)

    def getMessageId(self):
        return int(str(self.messageId), 2)

