import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.option_add('*font',('verdana', 12, 'bold'))
        self.title("MYGUI_3")
  
        ttk.Button(self, text='top').pack(side='top',expand='yes', anchor='w',fill='x')
        ttk.Button(self, text='CENTER').pack(side='top',expand='yes', anchor='w',fill='x')
        ttk.Button(self, text='Bottom').pack(side='top',expand='yes', anchor='w',fill='x')
         
        ttk.Button(self, text='left').pack(side='left')
        ttk.Button(self, text='This is Center Button').pack(side='left')
        ttk.Button(self, text='Right').pack(side='left')
        
if __name__ == "__main__":
    window:Window = Window()
    window.mainloop()