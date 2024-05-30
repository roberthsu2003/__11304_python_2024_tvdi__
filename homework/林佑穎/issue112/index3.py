<<<<<<< HEAD
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
        self.geometry("300x200")

        ttk.Button(self,text="Top").pack(fill="x")

        ttk.Button(self,text="Middle").pack(fill="x")

        ttk.Button(self,text="Bottom").pack(fill="x")
 
        
if __name__ == '__main__':
    window:Window = Window()
=======
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
        self.geometry("300x200")

        ttk.Button(self,text="Top").pack(fill="x")

        ttk.Button(self,text="Middle").pack(fill="x")

        ttk.Button(self,text="Bottom").pack(fill="x")
 
        
if __name__ == '__main__':
    window:Window = Window()
>>>>>>> 1d7693e809b33c94a219a3c6b1e12a8c91520419
    window.mainloop()