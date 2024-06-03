import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("計算機")
        self.geometry("500x200")
        self.var1 = tk.StringVar(value='')
        self.varop = tk.StringVar(value='')
        self.var2 = tk.StringVar(value='')


        ttk.Button(self,text="1",command=self.setvalue("1")).pack(side="left")
        ttk.Button(self,text="+",command=self.setvalue("+")).pack(side="left")
        ttk.Button(self,text="2",command=self.setvalue("2")).pack(side="left")
        
        ttk.Button(self,text="計算",command=self.calculate).pack(side="bottom")


    def setvalue(self,value):
        if value =="1":
            self.var1.set("1")
        elif value =="2":
            self.var2.set("2")
        elif value =="+":
            self.varop.set("+")


    def getequation(self):
        equation=f"{self.var1.get()}{self.varop.get()}{self.var2.get()}"
        return equation

    def calculate(self):

        try:
            ans = eval(self.getequation())
            ttk.Label(text=f"答案= {ans}").pack(pady=10)
        except Exception as e:
            ttk.Label(text=e).pack()



    

if __name__ =="__main__":
    window=Window()
    window.mainloop()


