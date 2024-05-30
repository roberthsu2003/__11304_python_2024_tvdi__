import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("New Word")
        self.geometry('300x300')

        ttk.Button(self,text="Boss").pack(expand=1,fill='x')

        ttk.Button(self,text="Manager").pack(side='top',expand=1,fill='x')

        ttk.Button(self,text="Team Leader").pack(expand=1,fill='x')

        ttk.Button(self,text="Specialist1").pack(side='left',padx='8')

        ttk.Button(self,text="Specialist2").pack(side='left',padx='8')

        ttk.Button(self,text="Specialist3").pack(side='left',padx='8')

if __name__ == '__main__':

    window:Window = Window()
    window.mainloop()