import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("!")
        self.geometry('300x200')
        
        ttk.Button(self,text="?").pack(side='left')  

        ttk.Button(self,text="??").pack(side='left')  

        ttk.Button(self,text="???").pack(side='left')
        


if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()