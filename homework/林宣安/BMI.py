from tkinter import ttk, Tk, Frame, Misc, messagebox
from tkinter.simpledialog import Dialog
import tkinter as tk

class BMICalculator:
    def __init__(self, name, height_cm, weight_kg):
        self.name = name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def calculate_bmi(self):
        try:
            height_m = self.height_cm / 100
            bmi = self.weight_kg / (height_m ** 2)
            return round(bmi, 2)
        except ZeroDivisionError:
            return None

class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI 計算器")

        # 允許視窗可調整大小
        self.root.resizable(True, True)

        # 自動調整佈局
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)

        self.create_widgets()

    def create_widgets(self):
        # 姓名標籤和輸入框
        self.name_label = ttk.Label(self.root, text="姓名:", foreground="black", font="Helvetica 10 bold")
        self.name_label.grid(column=0, row=0, padx=10, pady=5, sticky=tk.E)
        
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(column=1, row=0, padx=10, pady=5)

        # 身高標籤和輸入框
        self.height_label = ttk.Label(self.root, text="身高 (cm):", foreground="black", font="Helvetica 10 bold")
        self.height_label.grid(column=0, row=1, padx=10, pady=5, sticky=tk.E)
        
        self.height_entry = ttk.Entry(self.root)
        self.height_entry.grid(column=1, row=1, padx=10, pady=5)

        # 體重標籤和輸入框
        self.weight_label = ttk.Label(self.root, text="體重 (kg):", foreground="black", font="Helvetica 10 bold")
        self.weight_label.grid(column=0, row=2, padx=10, pady=5, sticky=tk.E)
        
        self.weight_entry = ttk.Entry(self.root)
        self.weight_entry.grid(column=1, row=2, padx=10, pady=5)

        # 計算按鈕
        self.calculate_button = ttk.Button(self.root, text="計算 BMI", command=self.calculate_bmi)
        self.calculate_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        # BMI 結果標籤
        self.result_label = ttk.Label(self.root, text="BMI:", foreground="black", font="Helvetica 10 bold")
        self.result_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

    def calculate_bmi(self):
        try:
            name = self.name_entry.get()
            height_cm = float(self.height_entry.get())
            weight_kg = float(self.weight_entry.get())

            bmi_calculator = BMICalculator(name, height_cm, weight_kg)
            bmi = bmi_calculator.calculate_bmi()

            if bmi:
                self.result_label.config(text=f"BMI: {bmi}")
                self.show_bmi_category(name, bmi)
            else:
                self.result_label.config(text="BMI: 計算錯誤")
        except ValueError:
            messagebox.showerror("輸入錯誤", "請輸入有效的數字")

    def show_bmi_category(self, name, bmi):
        if bmi < 18.5:
            extra_weight = round(18.5 - bmi, 2)
            category = "過輕"
            color = "green"
            suggestion = f"再增重{extra_weight}公斤就到正常體重了。"
        elif 18.5 <= bmi < 24.9:
            category = "正常"
            color = "blue"
            suggestion = "保持目前的體重。"
        elif 25 <= bmi < 29.9:
            extra_weight = round(bmi - 24.9, 2)
            category = "過重"
            color = "red"
            suggestion = f"再減{extra_weight}公斤就回到正常體重了。"
        else:
            category = "肥胖"
            color = "red"
            suggestion = "大幅度減重。"

        message = f"{name} 您好\n您的體重：{category}\n建議：{suggestion}"

        ShowInfo(parent=self.root, title="BMI 計算結果", message=message, category=category)


class ShowInfo(Dialog):
    def __init__(self, parent: Misc, title: str | None = None, message: str = "", category: str = ""):
        self.message = message
        self.category = category
        super().__init__(parent=parent, title=title)

    def body(self, master: Frame) -> Misc | None:
        text = tk.Text(self, height=5, font=('Helvetica', 12), width=40)
        text.pack(padx=10, pady=10)

        text.tag_configure("green", foreground="green")
        text.tag_configure("blue", foreground="blue")
        text.tag_configure("red", foreground="red")

        lines = self.message.split("\n")
        for line in lines:
            if "過輕" in line:
                text.insert(tk.END, line + "\n", "green")
            elif "正常" in line:
                text.insert(tk.END, line + "\n", "blue")
            elif "過重" in line or "肥胖" in line:
                text.insert(tk.END, line + "\n", "red")
            else:
                text.insert(tk.END, line + "\n")

        if self.category == "過輕":
            text.tag_add("green", "2.5", "2.7")
        elif self.category == "正常":
            text.tag_add("blue", "2.5", "2.7")
        elif self.category == "過重":
            text.tag_add("red", "2.5", "2.7")
        elif self.category == "肥胖":
            text.tag_add("red", "2.5", "2.7")

        text.config(state='disabled')
        return None

    def buttonbox(self) -> None:
        '''
        自訂button
        '''
        box = tk.Frame(self)
        self.ok_button = tk.Button(box, text="確定", width=10, command=self.ok)
        self.ok_button.pack(pady=(20, 30), ipady=10)
        box.pack()

    def ok(self) -> None:
        super().ok()

def main():
    root = Tk()
    app = BMICalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()