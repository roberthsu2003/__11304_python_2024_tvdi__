import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import Dialog


class BMIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BMI 計算器")
        self.configure(bg='#FCE2FE')  # 设置窗口背景色
    

         # Label 是 tkinter 裡用來建立文字或圖片的標籤物件,grid
        ttk.Label(self, text="姓  名  :", background='#FCE2FE', foreground='#A867DD', font=('微軟正黑體', 12)).grid(row=0, column=0, padx=10, pady=5)
        ttk.Label(self, text="身高 (公分):", background='#FCE2FE', foreground='#A867DD', font=('微軟正黑體', 12)).grid(row=1, column=0, padx=10, pady=5)
        ttk.Label(self, text="體重 (公斤):", background='#FCE2FE', foreground='#A867DD', font=('微軟正黑體', 12)).grid(row=2, column=0, padx=10, pady=5)
        

        self.name_entry = ttk.Entry(self)   #Entry 單行輸入框
        self.height_entry = ttk.Entry(self)
        self.weight_entry = ttk.Entry(self)

        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.height_entry.grid(row=1, column=1, padx=10, pady=5)
        self.weight_entry.grid(row=2, column=1, padx=10, pady=5)

        # button按钮
        self.calc_button = tk.Button(self, text="計 算 B M I", command=self.calculate_bmi, font=('微軟正黑體', 14), bg='#FCE2FE', fg='#A867DD')
        self.calc_button.grid(row=3, column=0, columnspan=2, pady=10,ipadx=50,ipady=10)
       

    def calculate_bmi(self):
        try:
            name = self.name_entry.get()
            height_cm = float(self.height_entry.get())
            weight_kg = float(self.weight_entry.get())
            height_m = height_cm / 100
            bmi = weight_kg / (height_m ** 2)

            if bmi < 18.5:
                status = '過輕\n建議:增加營養攝取，均衡飲食，多運動，維持健康體重'
                color = 'red'
            elif 18.5 <= bmi < 24:
                status = '健康\n繼續保持良好的生活習慣，維持健康體重'
                color = 'green'
            elif 24 <= bmi < 27:
                status = '過重\n建議:適當運動，控制飲食，保持健康的生活方式'
                color = 'red'
            elif 27 <= bmi < 30:
                status = '輕度肥胖\n建議:增加運動量，改善飲食習慣，定期健康檢查'
                color = 'red'
            elif 30 <= bmi < 35:
                status = '中度肥胖\n建議:積極減重，遵循健康飲食計劃，增加運動\n並諮詢醫療專業人員'
                color = 'red'
            else:
                status = '重度肥胖\n建議:緊急減重，遵循醫生建議，進行專業的減重計劃\n並定期進行健康檢查'
                color = 'red'

            ResultDialog(self, name, bmi, status, color)
        except ValueError:
            messagebox.showerror("輸入錯誤", "請輸入有效的數字")


class ResultDialog(Dialog):
    def __init__(self, parent, name, bmi, status, color):
        self.name = name
        self.bmi = bmi
        self.status = status
        self.color = color
        
        super().__init__(parent, title="快看看自己的B M I結果吧")
         

    def body(self, master):
        master.configure(bg='#FCE2FE')
        label1 = tk.Label(master, text=f"{self.name}你好：", font=('微軟正黑體', 14), fg='#A867DD', bg='#FCE2FE')
        label1.pack(padx=20, pady=5)
        
        label2 = tk.Label(master, text=f"你的BMI為: {self.bmi:.2f}", font=('微軟正黑體', 14), fg='#A867DD', bg='#FCE2FE')
        label2.pack(padx=20, pady=5)
        
        label3 = tk.Label(master, text=f"體重狀態：{self.status}", font=('微軟正黑體', 10), fg=self.color, bg='#FCE2FE')
        label3.pack(padx=20, pady=5)


if __name__ == "__main__":
    app = BMIApp()
    app.mainloop()
