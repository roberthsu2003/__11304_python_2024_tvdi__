import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
        self.geometry('500x200')
<<<<<<< HEAD:window_layout/index2.py
=======

<<<<<<< HEAD:homework/陳明勝/issue#112/grid1.py
        ttk.Button(self,text='Left').pack(side='left')

        ttk.Button(self,text='This is the Center Button').pack(side='left')

        ttk.Button(self,text='Right').pack(side='right') 
=======
        ttk.Button(self,text="Left").pack(side='left')
>>>>>>> 28d5b516c4ae7173f2ee6e899b694782b27f2f00:homework/周筱蘭/issue112/index2.py
>>>>>>> 5199e8297998685467a79a33b6319b16e80dc57b:homework/周筱蘭/issue112/index2.py
        
        ttk.Button(self,text="Left").pack(side='left')  

        ttk.Button(self,text="This is the Center Button").pack(side='left')  

        ttk.Button(self,text="Right").pack(side='left')
        


if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()