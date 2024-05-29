import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
        self.geometry("300x200")

        ttk.Button(self,text='Top').pack(fill='x',expand=1)

        ttk.Button(self,text='咪斗').pack(side='top',expand=1)

        ttk.Button(self,text='右').pack(side='right',fill='both',expand=1)

        ttk.Button(self,text='左').pack(side='right',fill='both',expand=1)

if __name__ == '__main__':
    window:Window=Window()
    window.mainloop()