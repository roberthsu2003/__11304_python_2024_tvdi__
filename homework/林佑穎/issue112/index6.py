import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack6")
        self.geometry("300x200")

        ttk.Button(self,text="left").pack(side="left",fill="both",expand=1)

        ttk.Button(self,text="Middle").pack(side="left",fill="both",expand=1)

        ttk.Button(self,text="right").pack(side="left",fill="both",expand=1)
 
        
if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()