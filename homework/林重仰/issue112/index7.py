import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("New Word")
        self.geometry('300x300')

        ttk.Button(self,text="Head").pack(side='top',expand=1,fill='x')

        ttk.Button(self,text="Body").pack(side='top',expand=1,fill='x')

        ttk.Button(self,text="Right Leg").pack(side='bottom')

        ttk.Button(self,text="Left Leg").pack(side='bottom')

if __name__ == '__main__':

    window:Window = Window()
    window.mainloop()