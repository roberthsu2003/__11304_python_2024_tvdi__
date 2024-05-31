### tkinter layout grid
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("Grid")
        self.geometry('300x300')
        
        ttk.Button(self, text = '(0,0)').grid(column=0,row=0)
        
        ttk.Label(self, text='A', background="#ff0").grid(column=0,row=1)
        
        ttk.Button(self, text = '(0,2)').grid(column=0,row=2)
        
        ttk.Label(self, text='B',background="#f0f").grid(column=0,row=3)
        
        ttk.Label(self, text='C',background="#0ff").grid(column=1,row=0)
        
        ttk.Button(self, text = '(2,0)').grid(column=2,row=0)
        
        ttk.Label(self, text='D',background="#0f0").grid(column=3,row=0)
        
        ttk.Button(self, text = '(1,1)').grid(column=1,row=1)

if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()