import tkinter as tk
from tkinter import ttk
from tkinter.constants import *

class Window(tk.Tk):
    def __init__(self,**kwargs): #**可有可無的隱數
        super().__init__(**kwargs) #呼叫父類別
        #多做一些事
        self.title("window3")  #參數
        self.geometry("300x200")  #視窗大小

        tk.Button(self,text="EAST").pack(side="right",padx=20) 
       
        tk.Button(self,text="SOUTH").pack(side="bottom",anchor='s',pady=20)
        
        tk.Button(self,text="WEST").pack(side="left",padx=20)

        tk.Button(self,text="NORTH").pack(side="top",pady=20)

if __name__ == '__main__':
    window:Window = Window()  
    window.mainloop() 
