import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack7")
        self.geometry("500x300")

        ttk.Button(self,text="left").pack(side="left",fill="both",expand=1,padx=10)

        ttk.Button(self,text="Middle").pack(side="left",fill="both",expand=1, padx=10)

        ttk.Button(self,text="right").pack(side="left",fill="both",expand=1,padx=10)
 
        
if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()