import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs): #**可有可無的隱數
        super().__init__(**kwargs) #呼叫父類別
        #多做一些事
        self.title("pack1")  #參數
<<<<<<< HEAD
        self.geometry("500x200")  #視窗大小

        ttk.Button(self,text="Left").pack(side="left")  #靠左
       

        ttk.Button(self,text="This is the Center Button").pack(side="left")
        

        ttk.Button(self,text="Right").pack(side="left")
=======
        self.geometry("300x200")  #視窗大小

        ttk.Button(self,text="ABC").pack(fill='y', side='left') 

        ttk.Button(self,text="ABC").pack(fill="x")
        

        ttk.Button(self,text="ABC").pack(fill='y', side="right")
>>>>>>> 5199e8297998685467a79a33b6319b16e80dc57b
        
      
if __name__ == '__main__':
    window:Window = Window()  
    window.mainloop() 
