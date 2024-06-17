import tkinter as tk  # Standard Tkinter module for GUI elements
from tkinter import ttk  # Tkinter's themed widgets
from ttkthemes import ThemedTk  # Allows usage of themed Tkinter windows
from tkinter import messagebox  # Standard message box dialogs
from tools import CustomMessagebox  # Custom message box for displaying results (assumed to be defined elsewhere)

# Define a class that inherits from ThemedTk
class Window(ThemedTk):
    # Initialize the class
    def __init__(self, theme: str | None, **kwargs):
        super().__init__(**kwargs)  # Initialize the parent class
        self.title("BMI計算器")  # Set the window title
        self.resizable(False, False)  # Disable window resizing
        
        # Configure styles for frames and buttons using ttk.Style()
        style = ttk.Style()
        style.configure('input.TFrame', background='#ffffff')
        style.configure('press.TButton', font=('arial', 16))
        
        # Create and pack the title frame and label
        titleFrame = ttk.Frame(self)
        title_label = ttk.Label(self, text="BMI計算器", font=("Arial", 20))
        title_label.pack(pady=10)
        titleFrame.pack(padx=100, pady=(0, 20))
        
        # Create and configure the input frame
        input_frame = ttk.Frame(self, style='Input.TFrame')
        
        # Name label and entry
        label_name = ttk.Label(input_frame, text="姓名:")
        label_name.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.name_value = tk.StringVar()
        self.name_value.set('')
        entry_name = ttk.Entry(input_frame, textvariable=self.name_value)
        entry_name.grid(row=0, column=1, padx=5, pady=5)
        
        # Height label and entry
        label_height = ttk.Label(input_frame, text="身高 (cm):")
        label_height.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.hight_value = tk.StringVar()
        self.hight_value.set('')
        entry_height = ttk.Entry(input_frame, textvariable=self.hight_value)
        entry_height.grid(row=1, column=1, padx=5, pady=5)
        
        # Weight label and entry
        label_weight = ttk.Label(input_frame, text="體重 (kg):")
        label_weight.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.weight_value = tk.StringVar()
        self.weight_value.set('')
        entry_weight = ttk.Entry(input_frame, textvariable=self.weight_value)
        entry_weight.grid(row=2, column=1, padx=5, pady=5)
        
        # Pack the input frame
        input_frame.pack(pady=10, padx=30)
        
        # Calculate button
        button_calculate = ttk.Button(self, text="計算", command=self.show_bmi_result, style='press.TButton')
        button_calculate.pack(side=tk.RIGHT, padx=(0, 35), pady=10, ipadx=10, ipady=15)
    
    # Method to show BMI result
    def show_bmi_result(self):
        try:
            # Get input values
            name: str = self.name_value.get()
            height: int = int(self.hight_value.get())
            weight: int = int(self.weight_value.get())
        except ValueError:
            # Show warning if input values are not valid integers
            messagebox.showwarning("Warning", "格式錯誤,欄位沒有填寫")
        except Exception:
            # Show warning for any other unknown errors
            messagebox.showwarning("Warning", "不知明的錯誤")
        else:
            # Call the method to display the result if inputs are valid
            self.show_result(name=name, height=height, weight=weight)
    
    # Method to display the result
    def show_result(self, name: str, height: int, weight: int):
        # Calculate BMI
        bmi = weight / (height / 100) ** 2
        
        # Determine the BMI status and advice
        if bmi < 18.5:
            status = "體重過輕"
            ideal_weight = 18.5 * (height / 100) ** 2
            weight_change = ideal_weight - weight
            status_color = "red"
            advice = f"您需要至少增加 {abs(weight_change):.2f} 公斤才能達到正常體重。"
        elif 18.5 <= bmi <= 24.9:
            status = "正常"
            status_color = "black"
            advice = "您的體重正常，請保持！"
        else:
            status = "體重過重"
            ideal_weight = 24.9 * (height / 100) ** 2
            weight_change = weight - ideal_weight
            status_color = "red"
            advice = f"您需要至少減少 {abs(weight_change):.2f} 公斤才能達到正常體重。"
        
        # Show the custom message box with the result
        CustomMessagebox(self, title="BMI", name=name, bmi=bmi, status=status, advice=advice)
    
    # Representation method
    def __repr__(self):
        return "我是window的實體"
            
# Main function to create and run the window
def main():
    window = Window(theme='arc')
    window.mainloop()

# Entry point check
if __name__ == '__main__':
    main()
