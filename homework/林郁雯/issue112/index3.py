import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs): #**可有可無的隱數
        super().__init__(**kwargs) #呼叫父類別
        #多做一些事
        self.title("pack1")  #參數
        self.geometry("300x200")  #視窗大小

<<<<<<< HEAD:homework/林郁雯/issue112/index3.py
        ttk.Button(self,text="Left").pack(side="top") 
       

        ttk.Button(self,text="This is the Center Button").pack(side="left")
=======
<<<<<<< HEAD:homework/林郁雯/issue112/index3.py
        ttk.Button(self,text="ABC").pack(side="top",fill="x") 
       

        ttk.Button(self,text="ABC").pack(fill='y', side='left')
=======
        tk.Button(self,text="EAST").pack(side="right",padx=20) 
       
        tk.Button(self,text="SOUTH").pack(side="bottom",anchor='s',pady=20)
>>>>>>> 278e4ac3dfddc9ac6df891b00621ad857414727f:homework/葉奕辰/issue112/index3.py
>>>>>>> 5199e8297998685467a79a33b6319b16e80dc57b:homework/葉奕辰/issue112/index3.py
        

<<<<<<< HEAD:homework/林郁雯/issue112/index3.py
        ttk.Button(self,text="Right").pack(side="right")
        
      
=======
<<<<<<< HEAD:homework/林郁雯/issue112/index3.py
        ttk.Button(self,text="ABC").pack(fill='y', side='right')
        
      
=======
>>>>>>> 278e4ac3dfddc9ac6df891b00621ad857414727f:homework/葉奕辰/issue112/index3.py
>>>>>>> 5199e8297998685467a79a33b6319b16e80dc57b:homework/葉奕辰/issue112/index3.py
if __name__ == '__main__':
    window:Window = Window()  
    window.mainloop() 
