import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        name = name_text.get("1.0", tk.END).strip()
        height_cm = float(height_text.get("1.0", tk.END).strip())
        weight_kg = float(weight_text.get("1.0", tk.END).strip())
        
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        
        if bmi < 18.5:
            state = "過輕"
            advice = "請確保您攝取足夠的營養。多吃高蛋白質和高熱量的食物，並進行適度的力量訓練以增加肌肉質量。"
            color = "red"
        elif 18.5 <= bmi < 24.9:
            state = "正常"
            advice = "恭喜您保持了健康的體重！請繼續保持均衡的飲食和規律的運動，保持身心健康。"
            color = "black"
        elif 25.0 <= bmi < 29.9:
            state = "過重"
            advice = "建議您注意飲食控制，減少高脂肪和高糖分的食物攝入。增加有氧運動，如跑步、游泳等，來減少體重。"
            color = "red"
        else:
            state = "肥胖"
            advice = "請務必關注您的飲食，選擇低熱量且富含纖維的食物。同時增加日常運動量，如步行、騎車等，逐步減少體重。"
            color = "red"
        
        message = f"您好, {name}!\n您的 BMI 值為: {bmi:.2f}\n"
        
        show_custom_dialog(name, bmi, state, advice, color)
    except ValueError:
        messagebox.showerror("輸入錯誤", "請輸入有效的數值。")

def show_custom_dialog(name, bmi, state, advice, color):
    dialog = tk.Toplevel(root)
    dialog.title("BMI 結果")

   
    frame = tk.Frame(dialog, padx=20, pady=20)
    frame.pack(fill='both', expand=True)

    tk.Label(frame, text=f"您好, {name}!", font=('Arial', 12, 'bold')).grid(row=0, column=0, sticky='w', pady=5)
    tk.Label(frame, text=f"您的 BMI 值為: {bmi:.2f}", font=('Arial', 12)).grid(row=1, column=0, sticky='w', pady=5)
    state_label = tk.Label(frame, text=f"您目前的體重狀態為: {state}", font=('Arial', 12), fg=color)
    state_label.grid(row=2, column=0, sticky='w', pady=5)
    tk.Label(frame, text=f"建議: {advice}", font=('Arial', 12), wraplength=400, justify='left').grid(row=3, column=0, sticky='w', pady=5)
    
    ok_button = tk.Button(frame, text="OK", command=dialog.destroy, width=10)
    ok_button.grid(row=4, column=0, pady=10)


root = tk.Tk()
root.title("BMI 計算器")


tk.Label(root, text="姓名:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
name_text = tk.Text(root, height=1, width=20, font=('Arial', 12, 'bold'))
name_text.grid(row=0, column=1, padx=10, pady=10, sticky='w')

tk.Label(root, text="身高 (cm):").grid(row=1, column=0, padx=10, pady=10, sticky='e')
height_text = tk.Text(root, height=1, width=20, font=('Arial', 12))
height_text.grid(row=1, column=1, padx=10, pady=10, sticky='w')

tk.Label(root, text="體重 (kg):").grid(row=2, column=0, padx=10, pady=10, sticky='e')
weight_text = tk.Text(root, height=1, width=20, font=('Arial', 12))
weight_text.grid(row=2, column=1, padx=10, pady=10, sticky='w')

calculate_button = tk.Button(root, text="計算", command=calculate_bmi)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
