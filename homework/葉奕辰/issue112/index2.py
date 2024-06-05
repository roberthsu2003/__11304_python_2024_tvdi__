import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs): #**可有可無的隱數
        super().__init__(**kwargs) #呼叫父類別
        #多做一些事
        self.title("window2")  #參數
        self.geometry("500x400")  #視窗大小

        tk.Button(self,text="Left",fg='#ff7f50',font=('arial',40,'italic')).pack(side='left')  #靠左
       

        tk.Button(self,text="Center Button",fg='#ff7f50',font=('arial',40,'italic')).pack(fill='x',anchor='center',side='left')
        

        tk.Button(self,text="Right",fg='#ff7f50',font=('arial',40,'italic'),bg='yellow').place(relx=0.4,rely=0.4,x=100,y=50)

if __name__ == '__main__':
    window:Window = Window()  
    window.mainloop() 
