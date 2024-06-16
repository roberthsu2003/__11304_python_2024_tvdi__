import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.simpledialog import Dialog
from ttkthemes import ThemedTk

class App(ThemedTk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.entry_name=""
        self.entry_height=""
        self.entry_weight=""
        self.window_design()
        self.title_design()
        self.input_design()
        self.button_design()

       
    def window_design(self):
        self.title("BMI計算器")
        self.resizable(False,False)
        
    def title_design(self):
        style = ttk.Style()
        #title frame內 有標題label
        main_frame=ttk.Frame(self)
        title_label=ttk.Label(self,text="BMI計算器", font=("Arial", 20))
        title_label.pack(pady=10)
        main_frame.pack(padx=100,pady=0)
    
    def input_design(self):
        #style設定傳入 ttk.Frame
        style=ttk.Style()
        style.configure("input.TFrame")
        input_frame =ttk.Frame(self,width=100,height=100,style="input.TFrame")
        
        label_name=ttk.Label(input_frame,text="姓名:",font=("Arial", 12))
        label_name.grid(row=0,column=0,padx=5,pady=5,sticky=tk.E)
        entry_name=ttk.Entry(input_frame)
        entry_name.grid(row=0,column=1,padx=5,pady=5)
        self.entry_name=entry_name

        label_height=ttk.Label(input_frame,text="身高(cm):",font=("Arial", 12))
        label_height.grid(row=1,column=0,padx=5,pady=5,sticky=tk.E)
        entry_height=ttk.Entry(input_frame)
        entry_height.grid(row=1,column=1,padx=5,pady=5)
        self.entry_height=entry_height

        label_weight=ttk.Label(input_frame,text="體重(kg):",font=("Arial", 12))
        label_weight.grid(row=2,column=0,padx=5,pady=5,sticky=tk.E)
        entry_weight=ttk.Entry(input_frame)
        entry_weight.grid(row=2,column=1,padx=5,pady=5)
        self.entry_weight=entry_weight

        input_frame.pack(padx=100,pady=30)

    def button_design(self):
        style=ttk.Style()
        style.configure("button.TButton",font=('arial',12))
        button_frame=ttk.Frame(self)
        ttk.Button(button_frame,text="計算BMI",command=self.show_BMI,style="button.TButton").pack()
        button_frame.pack(side="right",padx=(0,20),pady=10)
    
    def show_BMI(self):
        try:
            name=self.entry_name.get()
            height=int(self.entry_height.get())
            weight=int(self.entry_weight.get())
        except ValueError:
            messagebox.showwarning("Warning","數值錯誤")
        except Exception as error:
            messagebox.showwarning("Warning","格式錯誤")
        else:   
            self.calculate_BMI(name,height,weight)
            # BmiMseeageBox(parent=self,name=name,height=height
            #               ,weight=weight,bmi=bmi,title="BMI結果")

    def calculate_BMI(self,name,height,weight):
        bmi = round(weight / (height / 100) ** 2,2)
        if 18.5 <= bmi <= 24.9:
            status = "正常"
            status_color = "black"
            advice = "您的體重正常，請保持！"
        elif bmi < 18.5:
            status = "過輕"
            ideal_weight = round(18.5 * (height / 100) ** 2,2)
            weight_change = ideal_weight - weight
            status_color = "red"
            advice = f"需要至少增加 {abs(weight_change):.2f} 公斤才能達到正常體重。"
        else:
            status = "過重"
            ideal_weight = round(24.9 * (height / 100) ** 2,2)
            weight_change = weight - ideal_weight
            status_color = "red"
            advice = f"需要至少減少 {abs(weight_change):.2f} 公斤才能達到正常體重。"

        result_message = f"{name} 好:\nbmi:{bmi:.2f}\n體重:{status}\n建議:{advice}"

        
        BmiMessageBox(parent=self,message=result_message,status_color=status_color,title="BMI計算")



class BmiMessageBox(Dialog):
    def __init__(self,message,status_color,**kwargs):
        self.message=message
        self.status_color=status_color
        super().__init__(**kwargs)
        
    
    def body(self,master):
        text = tk.Text(master, height=8, padx=10, pady=10, font=("Arial", 15), width=40)
        text.pack()

        message_list=self.message.split("\n")
        for message in message_list:
            if("過輕" in message or "過重" in message):
                text.tag_configure("status_color", foreground=self.status_color)
                text.insert(tk.INSERT,message,"status_color")
                text.insert(tk.INSERT,"\n")
            else:
                text.insert(tk.INSERT,message)
                text.insert(tk.INSERT,"\n")

        text.config(state='disabled')

        return text

        