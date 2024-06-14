import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("你的名字")
        self.geometry('300x200')
        
        ttk.Button(self,text="雞雞").pack(fill='x')

        ttk.Button(self,text="掰掰").pack(fill='x')  

        ttk.Button(self,text="毛毛").pack(fill='x')
        


if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()