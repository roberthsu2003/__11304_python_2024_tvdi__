import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
     def __init__(self,**kwargs):
          super().__init__(**kwargs)
          self.title("pack1")
          self.geometry("500x200")

          ttk.Button(self,text="Left").pack(side="left",fill="both",expand=1)
          
          ttk.Button(self,text="This is Center Button").pack(side="left",fill="both",expand=1)

          ttk.Button(self,text="Right").pack(side="left",fill="both",expand=1)


if __name__=="__main__":
     window:Window=Window()
     window.mainloop()
     
