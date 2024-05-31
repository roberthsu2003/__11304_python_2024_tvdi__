import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("picture3")
        self.geometry('300x200')
        
        ttk.Button(self,text="Left").pack(side='left', expand='YES',fill='both')

        ttk.Button(self,text="Center").pack(side='left', expand='YES',fill='x')  

        ttk.Button(self,text="Right").pack(side='left', expand='YES',fill='y')
        


if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()
