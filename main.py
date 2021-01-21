# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Interfata import Aplicatie
from CoAP import *

text = ""
app = Aplicatie()
coap = Coap()
coap.start()

ip = '127.0.0.1'

port = 5006

def task():
    app.after(2000, task)
    (h, p, r, m, c) = app.take_data()
    print("cererea citita de pe interfata", r)
    run(h, p, r, m, c)
    app.update(text)


def run(my_host, my_port, my_cerere, my_metoda, my_type):
    global text
    if not my_cerere:
        coap.get(ip, port, "Score", COAP_TYPE.COAP_NONCON)
    else:
        if my_metoda == "Get":
            coap.get(my_host, my_port, str(my_cerere), my_type)
        elif my_metoda == "POST":
            coap.post(my_host, my_port, str(my_cerere), my_type)


    text = coap.getResult()




app.config(background="#ADD8E6")
app.mainloop()
