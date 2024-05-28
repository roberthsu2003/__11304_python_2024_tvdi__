import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack1")


if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()