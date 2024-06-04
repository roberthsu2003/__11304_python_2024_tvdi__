import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs): #**可有可無的隱數
        super().__init__(**kwargs) #呼叫父類別
        #多做一些事
        self.title("window1")  #參數

        width=600
        height=400
        window_width=self.winfo_screenwidth()
        window_height=self.winfo_screenheight()
        left=int((window_width-width)/2)
        top=int((window_height-height)/2)
        self.geometry(f'{width}x{height}+{left}+{top}')

        self.resizable(False,True)#x方向和y方向縮放

        self.configure(background='#000')

        tk.Button(self,text="Top",activeforeground='#f00',font=('arial',40,'bold')).pack(side='top',anchor='nw',padx=20,pady=20)

        tk.Button(self,text='Middle',activeforeground='#f00',font=('arial',40,'bold')).pack(side='right',anchor='ne',padx=40,pady=30)

        tk.Button(self,text='Bottom',activeforeground='#f00',font=('arial',40,'bold')).pack(side='bottom',anchor='s',pady=30)


if __name__ == '__main__':
    window:Window = Window()  
    window.mainloop() 
