import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.geometry('500x200')
        
        ttk.Button(self,text="Left").pack(side='left')

        ttk.Button(self,text="This is Bottom").pack(side='bottom')

        ttk.Button(self,text="right").pack(side='right')



if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()