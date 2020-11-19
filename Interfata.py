# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk
from tkinter import ttk

class Interfata(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        super().config(background="#ADD8E6")

        self.retea = tk.StringVar()
        self.locatie = tk.StringVar()
        self.port = tk.IntVar()
        self.resursa = tk.StringVar()
        self.metoda = tk.StringVar()
        self.confirmabil = tk.IntVar()

        combobox_resursa = ttk.Combobox(self, values=["resursa1", "resursa2", "resursa3", "resursa4", "resursa5"], textvariable=self.resursa, background="#ADD8E6")
        combobox_metoda = ttk.Combobox(self, values=["GET", "POST"], textvariable=self.metoda, background="#ADD8E6")
        spinbox_port = ttk.Spinbox(self, from_=0.0, to=1000, increment=1, textvariable=self.port, background="#ADD8E6")

        combobox_resursa.current(0)
        combobox_metoda.current(0)

        retea_label = ttk.Label(self, text="Retea", foreground="#0000A0", background="#ADD8E6")
        locatie_label = ttk.Label(self, text ="Locatie", foreground="#0000A0", background="#ADD8E6")

        retea_entry = ttk.Entry(self, textvariable=self.retea)
        locatie_entry = ttk.Entry(self, textvariable = self.locatie)

        port_label = ttk.Label(self, text="Port", foreground="#0000A0", background="#ADD8E6")
        resursa_label = ttk.Label(self, text="Resursa", foreground="#0000A0", background="#ADD8E6")
        metoda_label = ttk.Label(self, text="Metoda", foreground="#0000A0", background="#ADD8E6")
        confirmabil_label = ttk.Label(self, text="Confirmabil", foreground="#0000A0", background="#ADD8E6")

        buton_pornire = ttk.Button(self, text="Porneste aplicatia")
        buton_confirmare = ttk.Checkbutton(confirmabil_label, text="Confirmabil")

        retea_label.grid(row=1, column=14, sticky=tk.SE, pady=2)
        retea_entry.grid(row=1, column=15,sticky=tk.SE, pady=2)

        locatie_label.grid(row=3, column=14, sticky=tk.SE, pady=2)
        locatie_entry.grid(row=3, column=15, sticky=tk.SE, pady=2)

        port_label.grid(row=5, column=14, sticky=tk.SE, pady=2)
        spinbox_port.grid(row=5, column=15, sticky=tk.SE, pady=2)

        resursa_label.grid(row=7, column=14, sticky=tk.SE, pady=2)
        combobox_resursa.grid(row=7, column=15, sticky=tk.SE, pady=2)

        metoda_label.grid(row=9, column=14, sticky=tk.SE, pady=2)
        combobox_metoda.grid(row=9, column=15, sticky=tk.SE, pady=2)

        confirmabil_label.grid(row=11, column=14, sticky=tk.SE, pady=2)
        buton_confirmare.grid(row=11, column=15, sticky=tk.SE, pady=2)

        buton_pornire.grid(row=13, column=15, sticky=tk.SE, columnspan = 2)


class Aplicatie(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Aplicatie Client CoAP")
        self.geometry("300x200")

        self.resizable(width=False, height=False)

        Interfata(self).grid()


app = Aplicatie()
app.config(background="#ADD8E6")
app.mainloop()


