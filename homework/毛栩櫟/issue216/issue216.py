import tkinter as tk
from tkinter.simpledialog import Dialog
from tkinter import messagebox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('BMI計算器')
        
        self.name_label=tk.Label(self,text="姓名：",font=('微軟正黑體',20,'bold'))      #設定文字格式
        self.name_label.grid(row=0,sticky=tk.N,pady=20)                               #設定位置
        self.name_entry=tk.Entry(self,font=('標楷體',20),width=10)                     #設定答案欄格式
        self.name_entry.grid(row=0,column=1,sticky=tk.W,padx=10)                      #設定答案欄位置

        self.height_label=tk.Label(self,text="身高(cm)：",font=('微軟正黑體',20,'bold'))
        self.height_label.grid(row=1,sticky=tk.N,pady=20)
        self.height_entry=tk.Entry(self,font=('標楷體',20),width=10)
        self.height_entry.grid(row=1,column=1,sticky=tk.W,padx=10)

        self.weight_label=tk.Label(self,text="體重(kg)：",font=('微軟正黑體',20,'bold'))
        self.weight_label.grid(row=2,sticky=tk.N,pady=20)
        self.weight_entry=tk.Entry(self,font=('標楷體',20),width=10)
        self.weight_entry.grid(row=2,column=1,sticky=tk.W,padx=10)

        self.submit = tk.Button(self, text="提交", font=('微軟正黑體', 15, 'bold'), command=self.get_BMI,width=10)  #設定送出按鈕格式及指定功能
        self.submit.grid(row=3,column=1, pady=10)                                                                  #設定送出按鈕位置


    def get_BMI(self):        #將輸入的值送去計算
        try:                  #確保輸入的值是float
            N=self.name_entry.get()
            H=float(self.height_entry.get())
            W=float(self.weight_entry.get())
            if H=="" or H<=0 or H==False:
                messagebox.showerror("錯誤","請重新輸入身高")
                return
            elif W=="" or W<=0 or W==False:
                messagebox.showerror("錯誤","請重新輸入體重")
                return
        except Exception:
            messagebox.showerror("錯誤","請輸入數字")
            return
        Result(parent=self,name=N,height=H,weight=W)

class Result(Dialog):         #使用Dialog呈現
    def __init__(self,parent,name:str="",height:float="",weight:float=""):
        self.name=name
        self.height=height
        self.weight=weight
        super().__init__(parent)

    def body(self,master):
        self.title(f"{self.name}您好：")
        BMI=self.weight/((self.height/100)**2)
        tk.Label(master,text=f"BMI：{BMI:.1f}",font=('微軟正黑體',20,'bold')).grid(row=0,pady=10,sticky=tk.W)
        if BMI<18.5 :
            tk.Label(master,text=f"體重：{self.weight}公斤",font=('微軟正黑體',20,'bold'),fg="red").grid(row=1, pady=10,sticky=tk.W)
            tk.Label(master,text=f"建議：再增重{(18.5-BMI)*((self.height/100)**2):.1f}公斤，即可達正常範圍",font=('微軟正黑體',20,'bold')).grid(row=2, pady=10,sticky=tk.W)
        elif BMI >=24:
            tk.Label(master,text=f"體重：{self.weight}",font=('微軟正黑體',20,'bold'),fg="red").grid(row=1, pady=10,sticky=tk.W)
            tk.Label(master,text=f"建議：再減少{(BMI-24)*((self.height/100)**2):.1f}公斤，即可達正常範圍",font=('微軟正黑體',20,'bold')).grid(row=2, pady=10,sticky=tk.W)
        else:
            tk.Label(master,text=f"體重：{self.weight}",font=('微軟正黑體',20,'bold')).grid(row=1, pady=10,sticky=tk.W)
            tk.Label(master,text="建議：繼續保持",font=('微軟正黑體',20,'bold')).grid(row=2, pady=10,sticky=tk.W)   


cal = Window()
cal.mainloop()
