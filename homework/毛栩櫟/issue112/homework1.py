import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
        self.geometry("300x300")

        ttk.Button(self,text='上').pack(side='top')

        ttk.Button(self,text='下').pack(side='bottom')

        ttk.Button(self,text='左').pack(side='left')

        ttk.Button(self,text='右').pack(side='right')

if __name__ == '__main__':
    window:Window=Window()
    window.mainloop()