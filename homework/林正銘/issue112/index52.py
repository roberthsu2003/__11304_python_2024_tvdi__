import tkinter as tk
from tkinter import *

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.option_add('*font',('verdana', 20, 'bold'))
        self.title("林正銘_0528作業")

        fm = Frame(self)
        Button(fm, text='TOP').pack(side=TOP,expand=YES, anchor=W,fill=X)
        Button(fm, text='CENTER').pack(side=TOP,expand=YES, anchor=W,fill=X)
        Button(fm, text='Bottom').pack(side=TOP,expand=YES, anchor=W,fill=X)
        Button(fm, text='LEFT',background='#ff0').pack(side=LEFT)
        Button(fm, text='This is Center Button',background='#0f0').pack(side=LEFT)
        Button(fm, text='Right',background='#00f').pack(side=LEFT)
        fm.pack(fill=BOTH, expand=YES)

if __name__ == "__main__":
    window = Window()
    window.mainloop()