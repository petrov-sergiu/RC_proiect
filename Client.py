import socket
import threading
from random import randint

from Header import Header


class Caop:
    def __init__(self):
        self.sock = None
        self.port = 0

    def start(self, addr='', port=5006):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.bind(addr, port)

    def stop(self):
        if self.sock is not None:
            self.sock.close()
            self.sock = None

