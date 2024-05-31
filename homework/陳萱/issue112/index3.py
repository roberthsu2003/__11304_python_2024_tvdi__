import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("pack1")
        self.geometry('300x200')
        
        fm = ttk.Frame(self)
        ttk.Button(self,text="Left").pack(side='top',expand='YES')  

        ttk.Button(self,text="This is the Center Button").pack(side='top',expand='YES')  

        ttk.Button(self,text="Right").pack(side='top',expand='YES')

        fm.pack(fill='both',expand='YES')


if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()