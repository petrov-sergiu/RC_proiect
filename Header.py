def enum(**enums):
    return type('Enum', (), enums)

def CoapResponseCode(class_, detail):
    return ((class_ << 5) | (detail))

COAP_TYPE = enum(
    COAP_CON=0,
    COAP_NONCON=1,
    COAP_ACK=2,
    COAP_RESET=3
)

COAP_METHOD = enum(
    COAP_EMPTY=0,
    COAP_GET=1,
    COAP_POST=2
)

COAP_RESPONSE_CODE = enum(
    COAP_CREATED=[2,1],
    COAP_DELETED=[2, 2],
    COAP_VALID=[2, 3],
    COAP_CHANGED=[2, 4],
    COAP_CONTENT=[2, 5],
    COAP_BAD_REQUEST=[4, 0],
    COAP_UNAUTHORIZED=[4, 1],
    COAP_BAD_OPTION=[4, 2],
    COAP_FORBIDDEN=[4, 3],
    COAP_NOT_FOUND=[4, 4],
    COAP_METHOD_NOT_ALLOWD=[4, 5],
    COAP_NOT_ACCEPTABLE=[4, 6],
    COAP_PRECONDITION_FAILED=[4, 12],
    COAP_REQUEST_ENTITY_TOO_LARGE=[4, 13],
    COAP_UNSUPPORTED_CONTENT_FORMAT=[4, 15],
    COAP_INTERNAL_SERVER_ERROR=[5, 0],
    COAP_NOT_IMPLEMENTED=[5, 1],
    COAP_BAD_GATEWAY=[5, 2],
    COAP_SERVICE_UNAVALIABLE=[5, 3],
    COAP_GATEWAY_TIMEOUT=[5, 4],
    COAP_PROXYING_NOT_SUPPORTED=CoapResponseCode(5, 5)
)

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
        #8biti
        self.token=0

        self.code = None

    def setToken(self, tk):
        if((self.getTokenLength()>0) and (self.getTokenLength()<8)):
            self.token=format(tk, '0'+ str(self.getTokenLength()*8 + 'b'))

    def setHeader(self, version, typ, tokenLength):
        self.version = format(version, '02b')
        self.type = format(typ, '02b')
        self.tokenLength = format(tokenLength, '04b')

        self.header = (version << 6) + (typ << 4) + tokenLength
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

    def getToken(self):
        return int(str(self.messageId), 2)

    def buildHeader(self) -> str:
        self.header = "" + str(self.header) + str(self.code) + str(self.messageId)
        return self.header

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

