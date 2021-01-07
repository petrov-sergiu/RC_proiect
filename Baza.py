from Header import Header
from Mesaj import Mesaj

CON = 0
"""Mesaj cu confirmare."""

NON = 1
"""Mesaj fara confirmare."""

ACK = 2
"""Mesaj de tip acceptare."""

RST = 3
"""Mesaj de tip reset."""

types = {0: 'CON',
         1: 'NON',
         2: 'ACK',
         3: 'RST'}

EMPTY = 0
GET = 1
POST = 2
requests = {1: 'GET',
            2: 'POST'}

responses = {65: '2.01 Created',
             67: '2.03 Valid',
             132: '4.04 Not Found'}
