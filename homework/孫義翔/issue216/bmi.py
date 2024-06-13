import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        name = name_entry.get()
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = weight / ((height / 100) ** 2)

        if bmi < 18.5:
            bmi_category = "過輕。"
            suggestion = "建議增重。"
        elif 18.5 <= bmi < 24.9:
            bmi_category = "正常。"
            suggestion = "請保持。"
        else:
            bmi_category = "過重。"
            suggestion = "建議減重。"

        show_result(name, bmi, bmi_category, suggestion)

    except ValueError:
        messagebox.showerror("無效輸入", "請輸入有效的姓名、身高和體重數字。")


def show_result(name, bmi, bmi_category, suggestion):
    result_window = tk.Toplevel(root)
    result_window.title(f"{name} 的 BMI 結果")

    result_label = tk.Label(result_window, text=f"{name} 您好，\n您的 BMI 是: {bmi:.2f}\n體重分類: {bmi_category}\n建議: {suggestion}", justify="left")
    result_label.pack(padx=20, pady=20)
    ok_button = tk.Button(result_window, text="OK", command=lambda: result_window.destroy(),fg="white", bg="#D7B98E", bd=2)
    ok_button.pack(pady=10)


root = tk.Tk()

root.title("BMI 計算器")

name_label = tk.Label(root, text="姓名:")
name_label.config(font=("微軟正黑體", 12))
name_label.grid(row=0, column=0, padx=10, pady=5)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

height_label = tk.Label(root, text="身高 (cm):")
name_label.config(font=("微軟正黑體", 12))
height_label.grid(row=1, column=0, padx=10, pady=5)

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=5)

weight_label = tk.Label(root, text="體重 (kg):")
name_label.config(font=("微軟正黑體", 12))
weight_label.grid(row=2, column=0, padx=10, pady=5)

weight_entry = tk.Entry(root)
weight_entry.grid(row=2, column=1, padx=10, pady=5)


calculate_button = tk.Button(root, text="計算 BMI", command=calculate_bmi)
calculate_button.config(font=("Arial", 12), fg="white", bg="#D7B98E", bd=2)
calculate_button.grid(row=3, columnspan=2, pady=10)



root.mainloop()
