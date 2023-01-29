from tkinter import *
import webbrowser
from PIL import ImageTk, Image
from cats_ivedimas import *

langas = Tk()

class Kates():
    def __init__(self, main):
        self.main = main
        self.main.title("Kaciu registras")
        self.f_demo = Frame(self.main)


        self.main.mainloop()

    def close_window(self):
        self.main.destroy()

langas.mainloop()

