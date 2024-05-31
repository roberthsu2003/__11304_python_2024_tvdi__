import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("picture2")
        self.geometry('300x150')
        
        ttk.Button(self,text="1上",).pack(anchor='nw',padx=5,pady=4)  
        ttk.Button(self,text="2下").pack(anchor='ne')  
        ttk.Button(self,text="3上").pack(anchor='sw')
        ttk.Button(self,text="4下").pack(anchor='ne')

        

        
        
if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()