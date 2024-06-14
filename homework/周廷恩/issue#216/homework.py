import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import simpledialog, ttk
from ttkthemes import ThemedTk

class UserMessagebox(tk.Toplevel):
    def __init__(self, parent, title, message, status_color):
        super().__init__(parent)
        self.title(title)
        self.message = message
        self.status_color = status_color
        
        self.body()
        #self.buttonbox()
        
    def body(self,):
        self.message_text = tk.Text(self, font=("微軟正黑體", 10), wrap="word", height=5, width=40)
        self.message_text.insert(self.message)
        self.message_text.pack(padx=10, pady=10)

        if self.status_color:
            self.message_text.tag_add("status", "2.0", "2.end")
            self.message_text.tag_config("status", foreground=self.status_color)

    '''
    def buttonbox(self):
        self.ok_button = ttk.Button(self, text="計算", command=self.destroy)
        self.ok_button.pack(pady=10)
    '''
    

def bmi_result():
    try:
        name = entry_name.get()
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        bmi = weight / (height / 100) ** 2
        if bmi < 18.5:
            status = "過輕"
            ideal_weight = 18.5 * (height / 100) ** 2
            weight_change = ideal_weight - weight
            status_color = "red"
            advice = f"需要再增加 {abs(weight_change):.2f} 公斤才能達到正常體重。"
        elif 18.5 <= bmi <= 24.9:
            status = "正常"
            status_color = "black"
            advice = "體重正常，請保持！"
        else:
            status = "過重"
            ideal_weight = 24.9 * (height / 100) ** 2
            weight_change = weight - ideal_weight
            status_color = "red"
            advice = f"需要再減少 {abs(weight_change):.2f} 公斤才能達到正常體重。"
        
        result_message = f"Hello{name}!:\n   BMI指數:{bmi:.2f}\n   體重:{status}\n   建議:{advice}"

        # 顯示自定義的msgbox
        if status == "體重過輕" or status == "體重過重":
            dialog = UserMessagebox(root, title="BMI結果", message=result_message)
        else:
            messagebox.showinfo("BMI結果", result_message)

    except Exception as error:
           messagebox.showerror("輸入錯誤", "請輸入正確的身高(cm)和體重(kg)。")

# 建立主要視窗
root = ThemedTk(theme="arc")
root.title("BMI-計算器")
root.configure(bg="#ECB88A")  # 背景色
root.geometry("350x350")  # 設置窗口初始大小
root.resizable(False, False)  # 窗口大小不可調整(x,y)
style = ttk.Style()
style.theme_use('radiance')   #主題

# 設定按鈕外觀
style.configure('TButton', 
                foreground='black', 
                background='#E2943B', 
                borderwidth=0, 
                focusthickness=3, 
                focuscolor='none')
style.map('TButton', 
          background=[('active', '#E2943B')], 
          foreground=[('active', 'white')])

# 標題的Label
title_label = tk.Label(root, text="==BMI計算器==", font=("微軟正黑體", 16), bg="#E2943B")
title_label.pack(pady=10)

# 建立輸入區的特殊背景框
input_frame = tk.Frame(root, bg="#FAD689", padx=60, pady=10)
input_frame.pack(pady=10)

# 姓名
label_name = tk.Label(input_frame, text="姓名:", bg="white")
label_name.grid(row=0, column=0, padx=5, pady=5)

entry_name = tk.Entry(input_frame)
entry_name.grid(row=0, column=1, padx=5, pady=5)

# 身高體重
label_height = tk.Label(input_frame, text="身高 (cm):", bg="white")
label_height.grid(row=1, column=0, padx=5, pady=5)

entry_height = tk.Entry(input_frame)
entry_height.grid(row=1, column=1, padx=5, pady=5)

label_weight = tk.Label(input_frame, text="體重 (kg):", bg="white")
label_weight.grid(row=2, column=0, padx=5, pady=5)

entry_weight = tk.Entry(input_frame)
entry_weight.grid(row=2, column=1, padx=5, pady=5)

# 計算按鈕設計
button_calculate = ttk.Button(root, text="開始計算", command=bmi_result, style='TButton')
button_calculate.pack(pady=10)

# Run
root.mainloop()