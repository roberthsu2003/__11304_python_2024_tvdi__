### tkinter layout place
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("Place")
        self.geometry('400x350')
        
        ttk.Button(self, text = '(0,0)').place(x=0, y=0)
        
        ttk.Label(self, text='NORTH', background='#f90').place(x=150, y=0)
        
        ttk.Button(self, text = '(300,0)').place(x=300, y=0)
        
        ttk.Label(self, text='WEST', background='#09c').place(x=0, y=150)
        
        ttk.Button(self, text = '(0,300)').place(x=0, y=300)
        
        ttk.Label(self, text='MIDDLE', background='#fc0').place(x=150, y=150)
        
        ttk.Button(self, text = '(300,300)').place(x=300, y=300)
        
        ttk.Label(self, text='SOUTH', background='#f00').place(x=150, y=300)
        
        ttk.Label(self, text='EAST', background='#0c9').place(x=300, y=150)

if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()