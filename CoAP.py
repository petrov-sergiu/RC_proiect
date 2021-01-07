import socket
import select
from Header import *
from Mesaj import Mesaj
from random import randint
import threading


COAP_DEFAULT_PORT = 4321
COAP_DEFAULT_VERSION = 2
COAP_DEFAULT_TOKENL = 4
COAP_BUFFER_MAX_SIZE = 1024

COAP_DEFAULT_AKC_TIMEOUT = 2
COAP_DEFAULT_AKC_RANDOM_FACTOR = 1.5
COAP_DEFAULT_MAX_RETRANSMIT = 5
COAP_DEFAULT_TIMEOUT = 2

class Coap:
    def __init__(self):
        self.socket=None   #initializez socket cu none
        self.callbacks={} #initializare fucntie de callbacks
        self.responseCallback=None #raspunsul la functia callback initializat cu none
        self.port=0  #initializarea portului
        self.result="" #initializarea rezultatului

    def start(self,addr='0.0.0.0', port=COAP_DEFAULT_PORT): #functie de start comunicatie cu parametri: adresa si portul
        self.socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creaza un socket IPv4 (Internet, UDP),
        self.socket.bind((addr, port)) #Conectarea socketului la o adresa cunoscuta si la un port cunoscut

    def stop(self):#functie de stop comunicatie
        if self.socket is not None: #daca socket-ul meu este creat/exista atunci:
            self.socket.close() #Inchidem comunicatie/inchidem socket-ul
            self.socket=None #punem socketul pe valoarea none

    def sendPacket(self, ip, port, header, mesaj):#functie de trimitere a pachetului de date, parametri: adresa ip, portul header0ul si mesajul propriu-zis
        coapPacket=Mesaj() #initializare pachet coap cu mesajul (constructor din clasa Mesaj)
        coapPacket.createPacket(header, mesaj) #creare pachet cu header-ul si mesajul primite ca parametri
        status=0 #initializare status cu 0
        try:
            socketaddr=(ip, port) #initializare tuplei socketaddr cu adresa ip si port
            status=self.socket.sendto(coapPacket.getPackege(),socketaddr) #status ia valoarea trimsa catre server
            if(status>0): #daca este mai mare decat  0
                status=header.getMessageId() #pune in status valoare din header
            print('Pachet trimis. MessageId', status)
        except Exception as e:#exceptie daca status-ul este 0 atunci afisam mesaj de eroare
            status=0
            print('Exceptie la trimiterea pachetului!!!!')
        return status

    def send(self, ip, port, version, typ, tokenL,  metoda, token, payload):#functie de trimitere cu parametri adresa ip, portul, versiunea, tipul, dimensiune token, metoda, token-ul, data
        header=Header() #creare header
        header.setHeader(version, typ, tokenL) #stabilirea/crearea header-ului
        #token=randint(0, 65536) #token ia o valoare aleatoare data de un random
        #header.setToken(token)
        header.setCode(0, metoda) #stabilirea codului metodei utilizate
        return self.sendEx(ip, port,header, payload)

    def sendEx(self,ip, port, header, payload):
        nextMessage=randint(0, 65536)
        header.setMessageId(nextMessage)
        header.buildHeader()
        return self.loop(ip, port, header, payload, COAP_DEFAULT_MAX_RETRANSMIT)

    def sendResponse(self, ip, port, version, tokenL, mesajid, payload, code, token): #trimitere raspuns
        header=Header()
        header.setHeader(version, COAP_TYPE.COAP_ACK,tokenL) #setare header cu versiunea, mesajul de ACK si dim token-ului
        header.setCode(code[0], code[1]) #stabilirea codului
        header.setMessageId(mesajid) #setarea id-ului mesajului 16 biti
        #header.setToken(token)
        header.buildHeader() #construirea header-ului

        return self.sendPacket(ip, port, header, payload)  #trimiterea pachetului


    def readBytesFromSocket(self, nrBytes): #functie de citire a octetilor de pe socket UDP comunications
        try:
            return self.socket.recvfrom(nrBytes) #returneaza nr de octeti cititi de pe un sicket UDP
        except Exception:
            return None, None

    def get(self, ip, port, url, typ):
        return threading.Thread(target = self.send(ip, port, COAP_DEFAULT_VERSION, typ, 4, COAP_METHOD.COAP_GET, 0, url)).start()


    def post(self, ip, port, url,type ):
        return threading.Thread(target = self.send(ip, port, COAP_DEFAULT_VERSION,type, 4, COAP_METHOD.COAP_POST, 0, url )).start()

    def handleResponse(self, header, mesaj):
        header.print()
        self.result ="Mesajul este "+ str(mesaj)
        print("Mesajul receptionat de la server "+ str(mesaj))

    def getResult(self): #functie pentru obtinerea rezultatului
        return self.result

    def sendACK(self, ip, port, mesajid, token): #functie de trimitere a ACK
        header = Header()
        header.setHeader(COAP_DEFAULT_VERSION, COAP_TYPE.COAP_ACK, COAP_DEFAULT_TOKENL)
        header.setCode(0, 0)
        header.setMessageId(mesajid)
        #header.setToken(token)
        header.buildHeader()
        self.sendPacket(ip, port, header, "") #trimiterea pachetului catre server


    def codeGet(self,header):
        if header.getCodeClass() ==2 and header.getCodeDetail() ==3:
            print("COAP_VALID")
            return 1
        elif header.getCodeClass() ==2 and header.getCodeDetail() ==5:
            print("COAP_CONTENT")
            return 1
        elif header.getCodeClass() ==4 and header.getCodeDetail() ==5:
            print ("COAP_METHOD_NOT_ALLOWD")
        return 0

    def codePut(self, header):
        if header.getCodeClass() == 2 and header.getCodeDetail() == 1:
            print("COAP_CREATED")
            return 1
        if header.getCodeClass() == 2 and header.getCodeDetail() == 4:
            print("COAP_CHANGED")
            return 1
        if header.getCodeClass() == 4 and header.getCodeDetail() == 5:
            print("COAP_METHOD_NOT_ALLOWD")
        return 0

    def verifyCodeReceive(self, headerSent, headerReceive):
        if headerSent.getCode() == COAP_METHOD.COAP_GET:
            return self.codeGet(headerReceive)

        elif headerSent.getCode() == COAP_METHOD.COAP_POST:
            return self.codePut(headerSent)

    def loop(self, ip, port, header, mesaj, retransmit):
        global headerRcv














