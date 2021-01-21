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
    COAP_POST=2,
    COAP_PUT=3,
    COAP_DELETE=4
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



COAP_DEFAULT = enum(
    PORT = 5006,
    VERSION = 2, #versiunea
    TOKENL = 4, #dimensiunea tokenului
    BUFFER_MAX_SIZE = 1024,
    AKC_TIMEOUT = 2,
    AKC_RANDOM_FACTOR = 1.5,
    MAX_RETRANSMIT = 5,
    TIMEOUT = 2
)




