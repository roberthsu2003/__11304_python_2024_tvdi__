import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("訪問企鵝")
        self.geometry('300x200')
        
        ttk.Button(self,text="吃飯").pack(fill='both',expand=1)

        ttk.Button(self,text="睡覺").pack(fill='both',expand=1)  

        ttk.Button(self,text="打東東").pack(fill='both',expand=1)
        


if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()