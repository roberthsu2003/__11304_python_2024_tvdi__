import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs): #**可有可無的隱數
        super().__init__(**kwargs) #呼叫父類別
        #多做一些事
        self.title("pack1")  #參數
        self.geometry("300x300")  #視窗大小

        ttk.Button(self,text="ABC").pack(side="top")  
       

        ttk.Button(self,text="ABC").pack(side="left")
        

        ttk.Button(self,text="ABC").pack(side="right")
        ttk.Button(self,text="ABC").pack(side="bottom")
        
      
if __name__ == '__main__':
    window:Window = Window()  
    window.mainloop() 
