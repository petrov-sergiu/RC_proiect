'''from Header import Header
from Mesaj import Mesaj

import socket

ip = '0.0.0.0'
port = 4321
version = 1
tokenLen = 4

header = Header()
header.setHeader(version, 2, tokenLen)
header.setCode(0, 1)
header.setMessageId(29)
header.buildHeader()
header.print()


package = Mesaj()
package.createPacket(header, " MESAJ")
print(package.getPackege())
print("Token= " + str(header.getToken()))


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Activare optiune transmitere pachete de difuzie
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.connect(('127.0.0.1', 5006))

s.sendto(package.getPackege(), ('127.0.0.1', 5006))'''

import socket
from Mesaj import Mesaj
from CoAP import *
from Header import *

pack=Mesaj();
version = 1
tokenLen = 8
header = Header()
header.setHeader(version, 2, tokenLen)
header.setCode(2, 1)
header.setMessageId(29)
header.buildHeader()
header.print()

pack.createPacket(header, "Mesaj1")
#print(header.getToken())
print(pack.getPackege())

r=Coap()
r.start('127.0.0.1', 20001)

#hreading.Thread(target=r.send("127.0.0.1", 20001, COAP_DEFAULT.VERSION, 10, 4, COAP_METHOD.COAP_GET, 0, url)).start()

r.sendPacket("127.0.0.1",20001,header,"Mesaj123")
'''
bytesToSend         = header.getPackege()
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
stat=0
stat=UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0])

print(msg)

print(stat)'''

