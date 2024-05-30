<<<<<<< HEAD
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
        self.geometry("500x200")

        ttk.Button(self,text="Left").pack(side="left")

        ttk.Button(self,text="This is the Center Button").pack(side="left")

        ttk.Button(self,text="Right").pack(side="left")
 
        
if __name__ == '__main__':
    window:Window = Window()
=======
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
        self.geometry("500x200")

        ttk.Button(self,text="Left").pack(side="left")

        ttk.Button(self,text="This is the Center Button").pack(side="left")

        ttk.Button(self,text="Right").pack(side="left")
 
        
if __name__ == '__main__':
    window:Window = Window()
>>>>>>> 1d7693e809b33c94a219a3c6b1e12a8c91520419
    window.mainloop()