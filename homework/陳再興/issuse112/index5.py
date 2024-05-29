import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.geometry('500x200')
        
        ttk.Button(self,text="Left").pack(side='left')

        ttk.Button(self,text="This is the Center Button").pack(side='left')

        ttk.Button(self,text="right").pack(side='left')



if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()