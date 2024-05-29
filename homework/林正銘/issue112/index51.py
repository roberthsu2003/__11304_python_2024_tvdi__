import tkinter as tk
from tkinter import *

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.option_add('*font',('verdana', 20, 'bold'))
        self.title("林正銘_0528作業")
        self.geometry('300x200')

        fm = Frame(self)
        Button(fm, text='TOP').pack(side=TOP,fill='both',expand=1)
        Button(fm, text='left').pack(side=LEFT,fill='both',expand=1)
        Button(fm, text='Right').pack(side=LEFT,fill='both',expand=1)
        fm.pack()

if __name__ == "__main__":
    window = Window()
    window.mainloop()