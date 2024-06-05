import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack5")
        self.geometry("500x500")

        ttk.Button(self,text="top").pack(side="top")

        ttk.Button(self,text="left").pack(side="left")

        ttk.Button(self,text="Right").pack(side="right")

        ttk.Button(self,text="bottom").pack(side="bottom")
 
        
if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()