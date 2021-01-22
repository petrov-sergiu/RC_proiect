import tkinter as tk
from tkinter import ttk
from CoAP import *

console="alfa"
class Interfata(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        super().config(background="#ADD8E6")

        self.retea = tk.StringVar()
        self.port = tk.IntVar()
        self.resursa = tk.StringVar()
        self.metoda = tk.StringVar()
        self.confirmabil = tk.IntVar()
        self.retea.set("127.0.0.1")
        self.port.set(20001)
        self.out = tk.StringVar()
        combobox_resursa = ttk.Combobox(self, values=["resursa1", "resursa2", "resursa3", "resursa4", "resursa5"], textvariable=self.resursa, background="#ADD8E6")
        combobox_metoda = ttk.Combobox(self, values=["GET", "POST"], textvariable=self.metoda, background="#ADD8E6")
        spinbox_port = ttk.Spinbox(self, from_=0.0, to=30000, increment=1, textvariable=self.port, background="#ADD8E6")

        combobox_resursa.current(0)
        combobox_metoda.current(0)

        retea_label = ttk.Label(self, text="Retea", foreground="#0000A0", background="#ADD8E6")


        retea_entry = ttk.Entry(self, textvariable=self.retea)


        port_label = ttk.Label(self, text="Port", foreground="#0000A0", background="#ADD8E6")
        resursa_label = ttk.Label(self, text="Resursa", foreground="#0000A0", background="#ADD8E6")
        metoda_label = ttk.Label(self, text="Metoda", foreground="#0000A0", background="#ADD8E6")
        confirmabil_label = ttk.Label(self, text="Confirmabil", foreground="#0000A0", background="#ADD8E6")

        output_label = ttk.Label(self, textvariable=self.out, wraplength=600)

        buton_pornire = ttk.Button(self, text="Porneste aplicatia", command=self.change)
        buton_confirmare = ttk.Checkbutton(confirmabil_label, text="Confirmabil", variable=self.confirmabil)

        retea_label.grid(row=1, column=14, sticky=tk.SE, pady=2)
        retea_entry.grid(row=1, column=15, sticky=tk.SE, pady=2)


        port_label.grid(row=5, column=14, sticky=tk.SE, pady=2)
        spinbox_port.grid(row=5, column=15, sticky=tk.SE, pady=2)

        resursa_label.grid(row=7, column=14, sticky=tk.SE, pady=2)
        combobox_resursa.grid(row=7, column=15, sticky=tk.SE, pady=2)

        metoda_label.grid(row=9, column=14, sticky=tk.SE, pady=2)
        combobox_metoda.grid(row=9, column=15, sticky=tk.SE, pady=2)

        confirmabil_label.grid(row=11, column=14, sticky=tk.SE, pady=2)
        confirmabil_label.grid(row=11, column=14, sticky=tk.SE, pady=2)
        buton_confirmare.grid(row=11, column=15, sticky=tk.SE, pady=2)

        buton_pornire.grid(row=13, column=15, sticky=tk.SE, columnspan = 2)
        output_label.grid(row=15, column=0, columnspan=3)


    def change(self):
        global host, port, resource, request, confirmable

        if ((self.retea != "") and (self.port !="") and (self.resursa !="") and (self.metoda !="")):
            host, port, resource, request, confirmable=self.takeData()
            self.out.set(console)
        print("conectare")
        (h, p, r, m, c) = self.takeData()
        print("cererea citita de pe interfata", r)
        print(m)
        run(h, p, r, m, c)
        app.update(text)



    def takeData(self):
        return self.retea.get(), self.port.get(), self.resursa.get(), self.metoda.get(), self.confirmabil.get()


class Aplicatie(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Aplicatie Client CoAP")
        self.geometry("300x200")

        self.data = ""

        self.resizable(width=False, height=False)

        Interfata(self).grid()
        self.columnconfigure(0, weight=1)

    def takeData(self):
        return host, port, resource, request, confirmable
    def update(self, data):
        global console
        self.data += data
        console=data


text = ""
app = Aplicatie()
coap = Coap()
coap.start()

ip = '127.0.0.1'

port = 5006



def run(my_host, my_port, my_cerere, my_metoda, my_type):
    global text
    print("HELLO")
    if not my_cerere:
        coap.get(ip, port, "Mesaj", COAP_TYPE.COAP_NONCON)
    else:
        if my_metoda == "GET":
            coap.get(my_host, my_port, str(my_cerere), my_type)
        elif my_metoda == "POST":
            coap.post(my_host, my_port, str(my_cerere), my_type)


    text = coap.getResult()



if __name__ == '__main__':
    app.config(background="#ADD8E6")
    app.mainloop()
