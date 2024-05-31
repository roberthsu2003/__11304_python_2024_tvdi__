import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.equation_str=""

        self.title("加法機")
        self.label = ttk.Label(self, text="計算機")
        self.label.pack(fill="both", expand=1, padx=100, pady=30)

        number_one=ttk.Button(self,text="1",command=self.SetNumber(1))
        number_one.pack(side="left")

        number_two=ttk.Button(self,text="+",command=self.SetNumber("+"))
        number_two.pack(side="left")

        number_three=ttk.Button(self,text="2",command=self.SetNumber(2))
        number_three.pack(side="left")
        #使用 command指令 呼叫 Calculate來做計算
        equal_button=ttk.Button(self,text="=",command=self.Calculate)
        equal_button.pack(side="right")

    def Calculate(self):
        try:
            ans = eval(self.equation_str)
            self.label.configure(text=ans)
            self.equation_str = ""
        except Exception as e:
            self.label.configure(text="Error")
            print("Error:", e)

    def SetNumber(self,num):
        self.equation_str+=str(num)


if __name__ == "__main__":
    window = Window()
    window.mainloop()


