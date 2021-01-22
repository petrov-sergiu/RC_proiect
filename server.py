import socket
from _thread import *
import threading
from Header import Header
from Mesaj import Mesaj

import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

packRecv = Mesaj()
headerRecv = Header()
headerSend = Header()


#Creare pachet gol
emptyH=Header()
emptyMes=Mesaj()
emptyH.setHeader(1,2,4)
emptyH.setCode(0,0)
emptyH.setMessageId(33)
emptyH.setToken(70)
emptyH.buildHeader()
emptyMes.createPacket(emptyH, "gol")


msgFromServer = ""

bytesToSend = str.encode(msgFromServer)



# Create a datagram socket
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

sock.bind((localIP, localPort))

print("UDP server up and listening")

while(True):

    message,address = sock.recvfrom(bufferSize)

    if not message:
        break

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)


    print(clientMsg)
    print(clientIP)

    packRecv.setPack(message)
    head, mesg= packRecv.despachetarePacket()
    headerRecv.setHeader1(head)
    headerRecv.buildHeader()
    headerRecv.setCode(headerRecv.getCodeClass(), headerRecv.getCodeDetail())

    if headerRecv.getCode() !=0 :

        print("received",len(message), "bytes from ", address)
        print("data de la client ", message )

        if headerRecv.getMessageType() == 0:
            print(emptyMes.getPackege())
            sock.sendto(emptyMes.getPackege(),address)

        #if headerRecv.getMessageType() == 1:

    sock.sendall(emptyMes.getPackege())
