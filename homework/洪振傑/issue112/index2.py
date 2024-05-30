import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("XXX")
        self.geometry("300x200")


if __name__ == "__main__":
    window=Window()
    window.mainloop()
