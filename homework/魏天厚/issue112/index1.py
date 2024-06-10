import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("打老虎")
        self.geometry('300x200')
        
        ttk.Button(self,text="今晚").pack()  

        ttk.Button(self,text="明晚").pack()  

        ttk.Button(self,text="再說").pack()
        


if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()