### tkinter layout pack
import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("Pack")
        self.geometry("300x300")  
        
        ttk.Button(self, text = 'TOP').pack(side='top')
        ttk.Button(self, text = 'LEFT').pack(side='left')
        ttk.Button(self, text = 'BOTTOM').pack(side='bottom')
        ttk.Button(self, text = 'RIGHT').pack(side='right')
        
if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()