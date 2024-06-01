import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
        self.geometry('300x300')

        ttk.Button(self,text="Top").pack(fill='both',expand=1)
        

        ttk.Button(self,text="Middle").pack(fill='both',expand=1)
        

        ttk.Button(self,text="Bottom").pack(fill='both',expand=1)


if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()