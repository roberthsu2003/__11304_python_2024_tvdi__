import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("Track My Mood Today")
        self.geometry('500x500')

        ttk.Button(self, text='Happy').pack()
        ttk.Button(self, text='Neutral').pack()
        ttk.Button(self, text='Pissed').pack(fill='x')


if __name__ =='__main__':
    window:Window = Window()
    window.mainloop()