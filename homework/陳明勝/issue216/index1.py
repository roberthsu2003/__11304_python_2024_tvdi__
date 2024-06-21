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
    
    # 创建一个Label弹窗来展示结果，设置文本颜色为红色
    result_window = tk.Toplevel(self)
    result_window.title("BMI結果")
    result_label = Label(result_window, text=result_message, fg="red")
    result_label.pack(padx=20, pady=20)
