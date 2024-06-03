import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs): #**可有可無的隱數
        super().__init__(**kwargs) #呼叫父類別
        #多做一些事
        self.title("pack1")  #參數
        self.geometry("300x200")  #視窗大小

        ttk.Button(self,text="ABC").pack(fill='y', side='left') 

        ttk.Button(self,text="ABC").pack(fill="x")
        

        ttk.Button(self,text="ABC").pack(fill='y', side="right")
        
      
if __name__ == '__main__':
    window:Window = Window()  
    window.mainloop() 
