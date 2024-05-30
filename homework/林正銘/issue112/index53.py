import tkinter as tk
from tkinter import *

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.option_add('*font',('verdana', 20, 'bold'))
        self.title("林正銘_0528作業")

        fm = Frame(self)
        Button(fm, text='TOP',background='#ff0').pack(side=TOP,expand=YES, anchor=W,fill=X)
        Button(fm, text='CENTER',background='#BBB').pack(side=TOP,expand=YES, anchor=W,fill=X)
        Button(fm, text='Bottom',background='#088').pack(side=TOP,expand=YES, anchor=W,fill=X)
        fm.pack(side=LEFT, fill=BOTH, expand=YES)

        fm1 = Frame(self)
        Button(fm1, text='LEFT',background='#888').pack(side=LEFT)
        Button(fm1, text='Middle  Center',background='#BBB').pack(side=LEFT)
        Button(fm1, text='Right',background='#DDD').pack(side=LEFT)
        fm1.pack(side=LEFT, padx=10)

if __name__ == "__main__":
    window = Window()
    window.mainloop()