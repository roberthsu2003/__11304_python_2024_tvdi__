import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.option_add('*font',('verdana', 12, 'bold'))
        self.title("MyGUI_1")
        self.geometry("300x200")

        ttk.Button(self,text="Top").pack(side='top')
    
        ttk.Button(self,text="Left").pack(side='left')
    
        ttk.Button(self,text="Right").pack(side='right')

if __name__ == "__main__":
    window = Window()
    window.mainloop()