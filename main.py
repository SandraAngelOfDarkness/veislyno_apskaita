from tkinter import *
from kates import Kates

class MainApp():
    def __init__(self, main):
        self.main = main
        self.f_catalog = Frame(self.main)
        self.l_pasirinkimai = Label(self.f_catalog, width=10, text="Pasirinkite")
        self.b_kates = Button(self.f_catalog, width=10, text="Kaciu registras", command=self.run_kates)

        self.l_pasirinkimai.pack(side=TOP)
        self.b_kates.pack()
        self.f_catalog.pack()

    def run_kates(self):
        self.window_kates = Toplevel(self.main)
        self.app = Kates(self.window_kates)

