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


        ttk.Checkbutton(self,
                    text='10',
                    variable=self.var1,
                    onvalue='10',
                    offvalue='',
                    ).pack(side='left')
        
        ttk.Checkbutton(self,
                    text='2',
                    variable=self.var2,
                    onvalue='2',
                    offvalue='',
                    ).pack(side='right')
        
        ttk.Radiobutton(self,
                        text='+',
                        variable=self.varop,
                        value='+',
                        ).pack(side='top', pady=10)

        ttk.Radiobutton(self,
                        text='-',
                        variable=self.varop,
                        value='-',
                        ).pack(side='top', pady=10)

        ttk.Radiobutton(self,
                        text='x',
                        variable=self.varop,
                        value='*',
                        ).pack(side='top', pady=10)

        ttk.Radiobutton(self,
                        text='/',
                        variable=self.varop,
                        value='/',
                        ).pack(side='top', pady=10)
        
        
        ttk.Button(self,text="計算",command=self.calculate).pack(side="bottom")

        
    def setequation(self):
        equation=f"{self.var1.get()}{self.varop.get()}{self.var2.get()}"
        return equation

    def calculate(self):

        try:
            ans = eval(self.setequation())
            showinfo(title='Result', message=ans)
        except Exception as e:
            showinfo(title='Error', message=str(e))


    

if __name__ =="__main__":
    window=Window()
    window.mainloop()


