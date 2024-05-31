import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
     def __init__(self,**kwargs):
          super().__init__(**kwargs)
          self.title("Ian")
          self.geometry("300x200")

          ttk.Button(self,text="Top").pack(fill="x",padx=10)
          
          ttk.Button(self,text="Middle").pack(fill="x",padx=20)

          ttk.Button(self,text="Bottom").pack(fill="x",padx=30)


if __name__=="__main__":
     window:Window=Window()
     window.mainloop()
