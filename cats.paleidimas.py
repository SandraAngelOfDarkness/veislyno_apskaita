from tkinter import *
from main import MainApp
from PIL import ImageTk, Image
import tkinter as tk

pasirinkta = IntVar()

def run_main_app():
    root = tk.Tk()
    #icon = ImageTk.PhotoImage(Image.open('salad.ico'))
    #root.call('wm', 'iconphoto', root._w, icon)
    # root.iconbitmap(bitmap=r'salad.ico')
    root.title("Kaciu registras")
    root.geometry("500x500")
    app = MainApp(root)
    
    root.mainloop()


if __name__ == "__main__":
    run_main_app()

