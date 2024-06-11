import tkinter as tk
from tkinter import messagebox

def get_bmi():
    try:
        name = entry_name.get()
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())
        height_m = height_cm / 100
        bmi = weight / (height_m * height_m)
        
        if bmi < 18.5:
            category = "UNDERWEIGHT"
        elif 18.5 <= bmi < 24.9:
            category = "STANDARD"
        elif 25 <= bmi < 29.9:
            category = "OVERWEIGHT"
        else:
            category = "TOO FAT"
        
        ideal_weight_low = 18.5 * (height_m * height_m)
        ideal_weight_high = 24.9 * (height_m * height_m)

        message = (f"{name}，your BMI: {bmi:.1f} ({category})\n"
                   f"Your ideal weight is:  {(ideal_weight_low + ideal_weight_high)/2:.1f} kg")


        messagebox.showinfo("BMI Result", message)
    except ValueError:
        messagebox.showerror("Invalid answer. Please try again!")

def on_close():
    root.destroy()

root = tk.Tk()
root.title("Get My BMI")

root.geometry("300x300")

label_name = tk.Label(root, text="Name:")
label_name.pack(ipady=5)
entry_name = tk.Entry(root, width=15)
entry_name.pack(ipady=5)

label_height = tk.Label(root, text="Height (cm):")
label_height.pack(ipady=5)
entry_height = tk.Entry(root, width=15)
entry_height.pack(ipady=5)

label_weight = tk.Label(root, text="Weight (kg):")
label_weight.pack(ipady=5)
entry_weight = tk.Entry(root, width=15)
entry_weight.pack(ipady=5)


btn_calculate = tk.Button(root, text="Let's seee!", width=10, command=get_bmi)
btn_calculate.pack(pady=(10,10),ipady=10)

# btn_close = tk.Button(root, text="BYEEE", command=on_close)
# btn_close.pack(pady=5)

root.mainloop()