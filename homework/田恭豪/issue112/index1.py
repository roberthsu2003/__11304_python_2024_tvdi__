import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("picture1")
        self.geometry('300x150')
  
        
        ttk.Button(self,text="eyes").pack(side='left')
        ttk.Button(self,text="eyes").pack(side='right')  
        ttk.Button(self,text="mouth").pack(side='bottom')


if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()
