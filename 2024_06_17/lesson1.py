import tkinter as tk
from tkinter import ttk
from tkinter import Misc


class Example(ttk.Frame):
    def __init__(self,master:Misc,**kwargs):
        super().__init__(master=master,**kwargs)



def main():
    window = tk.Tk()
    window.title("Frame的繼承")
    window.geometry("400x250")
    window.mainloop()

if __name__ == "__main__":
    main()