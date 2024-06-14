import tkinter as tk
from tkinter import simpledialog, messagebox

class BMIDialog(simpledialog.Dialog):
    def __init__(self, parent, title, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        super().__init__(parent, title)
    
    def body(self, master):
        bmi = self.weight / ((self.height / 100) ** 2)
        
        if bmi < 18.5:
            suggestion = "你體重過輕了，建議增重。"
            ideal_weight = 18.5 * (self.height / 100) ** 2
            weight_diff = ideal_weight - self.weight
            suggestion += f" 建議增加至少 {weight_diff:.2f} 公斤。"
        elif 18.5 <= bmi < 24.9:
            suggestion = "你的體重在正常範圍內。保持下去！"
        else:
            suggestion = "你體重過重了，建議減重。"
            ideal_weight = 24.9 * (self.height / 100) ** 2
            weight_diff = self.weight - ideal_weight
            suggestion += f" 建議減少至少 {weight_diff:.2f} 公斤。"
        
        result = f"{self.name}你好:\n你的 BMI 是: {bmi:.2f}\n{suggestion}"
        
        label = tk.Label(master, text=result, wraplength=300)
        label.pack(padx=20, pady=20)
        return label


root = tk.Tk()
root.title("BMI 計算器")


tk.Label(root, text="姓名:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="身高 (cm):").grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="體重 (kg):").grid(row=2, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=2, column=1, padx=10, pady=5)


def calculate_bmi():
    try:
        name = name_entry.get()
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        BMIDialog(root, "BMI 結果", name, height, weight)
    except ValueError:
        messagebox.showerror("無效輸入", "請輸入有效的姓名、身高和體重數字。")


calculate_button = tk.Button(root, text="計算 BMI", command=calculate_bmi)
calculate_button.grid(row=3, columnspan=2, pady=10)


root.mainloop()
