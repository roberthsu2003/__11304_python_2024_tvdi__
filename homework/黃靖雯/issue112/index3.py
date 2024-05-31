import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("What Do You Wanna Eat")
        self.geometry('500x200')

        ttk.Button(self, text='Rice').pack(side='left', expand=False, fill='x')
        ttk.Button(self, text='Pizza').pack(side='left', expand=False, fill='x')
        ttk.Button(self, text='SUSHI').pack(side='left', expand=True, fill='x')


if __name__ =='__main__':
    window:Window = Window()
    window.mainloop()