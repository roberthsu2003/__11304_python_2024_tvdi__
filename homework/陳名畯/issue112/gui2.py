import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.option_add('*font',('verdana', 12, 'bold'))
        self.title("MYGUI_2")
        self.geometry("300x200")
   
        ttk.Button(self, text='Left').pack(side='left', expand='true',fill='both')

        ttk.Button(self, text='Center').pack(side='left', expand='true',fill='both')

        ttk.Button(self, text='Right').pack(side='left', expand='true',fill='both')
    
if __name__ == "__main__":
    window = Window()
    window.mainloop()

