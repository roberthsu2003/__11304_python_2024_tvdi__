import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
     def __init__(self,**kwargs):
          super().__init__(**kwargs)
          self.title("pack1")
          self.geometry("300x200")

          ttk.Button(self,text="Top").pack(side="left",expand=1,anchor="nw")
          
          ttk.Button(self,text="Middle").pack(side="right",expand=1,anchor="nw")

          ttk.Button(self,text="Bottom").pack(side="bottom",expand=1,anchor="sw")


if __name__=="__main__":
     window:Window=Window()
     window.mainloop()
