import tkinter as tk
from tkinter import ttk, messagebox

class BMI_Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BMI Calculator")
        
        self.name_var = tk.StringVar()
        self.height_var = tk.StringVar()
        self.weight_var = tk.StringVar()
        
        frame = ttk.Frame(self)
        frame.grid(row=0, column=0, padx=20, pady=20)
        
        ttk.Label(frame, text="姓名：").grid(row=0, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.name_var).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="身高(cm)：").grid(row=1, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.height_var).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="體重(kg)：").grid(row=2, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.weight_var).grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(frame, text="計算BMI", command=self.calculate_bmi).grid(row=3, columnspan=2, pady=10)
    
    def calculate_bmi(self):
        name = self.name_var.get()
        height_str = self.height_var.get()
        weight_str = self.weight_var.get()
        
        if not name:
            messagebox.showwarning("警告", "請輸入姓名")
            return
        if not height_str:
            messagebox.showwarning("警告", "請輸入身高")
            return
        if not weight_str:
            messagebox.showwarning("警告", "請輸入體重")
            return
        
        try:
            height = float(height_str) / 100  # 轉換成米
            weight = float(weight_str)
        except ValueError:
            messagebox.showerror("錯誤", "身高和體重必須為數字")
            return
        
        if height <= 0 or weight <= 0:
            messagebox.showerror("錯誤", "身高和體重必須為正數")
            return
        
        bmi = weight / (height ** 2)
        bmi_category = self.get_bmi_category(bmi)
        suggestion = self.get_suggestion(bmi_category, height)
        
        result_message = f"{name}您好:\n"
        result_message += f"您的BMI值為: {bmi:.2f}\n"
        result_message += f"您的體重是{bmi_category}\n"
        result_message += f"{(suggestion)}"
        
        messagebox.showinfo("BMI結果", result_message)
    
    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "過輕"
        elif bmi < 24:
            return "正常"
        else:
            return "過重"
    
    def get_suggestion(self, bmi_category, height):
        if bmi_category == "過輕":
            ideal_weight = 18.5 * (height ** 2)
            difference = round(ideal_weight - float(self.weight_var.get()), 2)
            return f"建議增胖 {difference} 公斤"
        elif bmi_category == "過重":
            ideal_weight = 24 * (height ** 2)
            difference = round(float(self.weight_var.get()) - ideal_weight, 2)
            return f"建議減輕 {difference} 公斤"
        else:
            return "很棒!!請繼續保持!"

if __name__ == "__main__":
    app = BMI_Calculator()
    app.mainloop()
