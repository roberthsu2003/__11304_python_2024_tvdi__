import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
<<<<<<< HEAD:homework/陳再興/issuse112/index5.py

        self.geometry('500x200')
        
        ttk.Button(self,text="Left").pack(side='left')

        ttk.Button(self,text="This is the Center Button").pack(side='left')

        ttk.Button(self,text="right").pack(side='left')

=======
        self.title("pack1")
        self.geometry('500x200')
        
        ttk.Button(self,text="Left").pack(side='right')  

        ttk.Button(self,text="This is the Center Button").pack(side='right')  

        ttk.Button(self,text="Right").pack(side='right')
        
>>>>>>> 5199e8297998685467a79a33b6319b16e80dc57b:homework/陳萱/issue112/index1.py


if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()