from Header import Header
from Mesaj import Mesaj



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
