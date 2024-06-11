import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox

class Window(ThemedTk):
    def __init__(self,theme:str|None,**kwargs):
        super().__init__(**kwargs)
        self.title("BMI計算器")
        #self.configure(bg="#D3D3D3")
        #self.geometry("350x350+100+50")
        self.resizable(False,False)
        style = ttk.Style()
        style.configure('input.TFrame',background='#ffffff')
        style.configure('press.TButton',font=('arial',16))
        #========================
        titleFrame = ttk.Frame(self)
        title_label = ttk.Label(self, text="BMI計算器", font=("Arial", 20))
        title_label.pack(pady=10)
        titleFrame.pack(padx=100,pady=(0,20))
        #========================
        input_frame = ttk.Frame(self,style='Input.TFrame')
        # 姓名
        label_name = ttk.Label(input_frame, text="姓名:")
        label_name.grid(row=0, column=0, padx=5, pady=5,sticky=tk.E)

        self.entry_name = ttk.Entry(input_frame)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        # 身高體重
        label_height = ttk.Label(input_frame, text="身高 (cm):")
        label_height.grid(row=1, column=0, padx=5, pady=5,sticky=tk.E)

        self.entry_height = ttk.Entry(input_frame)
        self.entry_height.grid(row=1, column=1, padx=5, pady=5)

        label_weight = ttk.Label(input_frame, text="體重 (kg):")
        label_weight.grid(row=2, column=0, padx=5, pady=5,sticky=tk.E)

        self.entry_weight = ttk.Entry(input_frame)
        self.entry_weight.grid(row=2, column=1, padx=5, pady=5)    

        input_frame.pack(pady=10,padx=30)
        #===================================

        button_calculate = ttk.Button(self, text="計算", command=self.show_bmi_result,style='press.TButton')
        button_calculate.pack(side=tk.RIGHT,padx=(0,35),pady=10,ipadx=10,ipady=15)

    
    def show_bmi_result(self):
        try:
            name:str = self.entry_name.get()
            height:int = int(self.entry_height.get())
            weight:int = int(self.entry_weight.get())
        except Exception as error:
            messagebox.showwarning("Warning","格式錯誤或欄位沒有填寫")

        print(name,height,weight)





def main():
    window = Window(theme='arc')
    window.mainloop()

if __name__ == '__main__':
    main()