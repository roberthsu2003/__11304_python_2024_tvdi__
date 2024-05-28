import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
        self.geometry("300x200")

        ttk.Button(self,text='ToP').pack()

        ttk.Button(self,text='咪斗').pack()

        ttk.Button(self,text='屁股').pack()

if __name__ == '__main__':
    window:Window=Window()
    window.mainloop()