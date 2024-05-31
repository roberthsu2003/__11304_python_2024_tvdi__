import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack3")
        self.geometry('300x300')

        ttk.Button(self,text="排隊囉").pack()
        ttk.Button(self,text="A1").pack()
        ttk.Button(self,text="A2").pack()
        ttk.Button(self,text="A3").pack()
        ttk.Button(self,text="A4").pack()
        ttk.Button(self,text="A5").pack()
        ttk.Button(self,text="A6").pack()
        ttk.Button(self,text="A7").pack()
        ttk.Button(self,text="A8").pack()



if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()