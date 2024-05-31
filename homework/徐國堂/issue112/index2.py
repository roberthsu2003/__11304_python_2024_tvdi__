import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
<<<<<<< HEAD:homework/徐國堂/issue112/index2.py
        self.geometry('500x200')
        
        ttk.Button(self,text="Left").pack(side='left')  
=======
        # self.geometry('500x200')
        
        ttk.Button(self,text="Left").pack(side='top')  
>>>>>>> 5199e8297998685467a79a33b6319b16e80dc57b:homework/陳萱/issue112/index2.py

        ttk.Button(self,text="This is the Center Button").pack(side='left')  

        ttk.Button(self,text="Right").pack(side='left')
        


if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()