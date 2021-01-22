import socket
from _thread import *
import threading
from Header import Header
from Mesaj import Mesaj

'''UDP_IP = '127.0.0.1'
UDP_PORT = 5006
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))



#lock = threading.Lock()
headerRecv = Header()
headerSend = Header()
packRecv = Mesaj()
packSend = Mesaj()
#headerSend.setHeader1(1,0,4)
headerSend.setCode(2,5)
headerSend.setMessageId(29)
headerSend.setToken(68)
headerSend.buildHeader()


#make an empty message
emptyM = Header()
emptyP = Mesaj()
#emptyM.setHeader1(1,2,4)
emptyM.setCode(0,0)
emptyM.setMessageId(30)
emptyM.setToken(70)
emptyM.buildHeader()
emptyP.createPacket(emptyM,"gool")

dataSent=""

print("-------------------------------------Wait connections-----------------------------------------")
while 1:
    data, addr = sock.recvfrom(1024)
    #lock.acquire()
    #start_new_thread(process, (addr, data,))
    if not data:
        break
    packRecv.set(data)
    head, mesg = packRecv.dispackPack()
    headerRecv.setHeader(head)
    headerRecv.buildHeader()
    headerRecv.setCode(headerRecv.getCodeClass(), headerRecv.getCodeDetail())
    if headerRecv.getCode() !=0 :

        print("received",len(data), "bytes from ", addr)
        print("data de la client ", mesg )
        if mesg == "SCORE":
            dataSent = "2-0"
        if mesg == "RedCards":
            dataSent = "3REdCards"
        if mesg == "YellowCars":
            dataSent = "8Yellow Cards"
        if mesg == "Corners":
            dataSent = "9Corners"
        if mesg =="Offsides":
            dataSent = "0Offisides"

        packSend.buildPack(headerSend, dataSent)
       # sock.sendto(emptyP.getPackege(), addr)
        headerSend.print()
        sock.sendto(packSend.getPackege(), addr)
        #sock.sendto(packSend.getPackege(), addr)
    else:
        print("ACK recive")

        

#sock.close()
'''
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
