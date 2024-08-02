import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# 定義自訂圖形函式
def distplot_features():
    # 假設這裡是某些特徵的分佈圖示例
    data = np.random.normal(loc=0, scale=1, size=1000)
    plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
    plt.title('特徵分佈示例')
    plt.xlabel('值')
    plt.ylabel('頻率')
    plt.grid(True)
    plt.tight_layout()

# 定義彈跳視窗函式
def click1():
    # 創建彈跳視窗
    popup = tk.Toplevel()
    popup.title("自訂圖形示例")

    # 呼叫自訂圖形函式並顯示在彈跳視窗中
    distplot_features()

    # 將 Matplotlib 圖形顯示在 Tkinter 中
    canvas = FigureCanvasTkAgg(plt.gcf(), master=popup)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # 添加一個關閉按鈕
    close_button = tk.Button(popup, text="關閉", command=popup.destroy)
    close_button.pack(pady=10)

# 建立主視窗
root = tk.Tk()
root.title("按下確認顯示自訂圖形的示例")

# 添加標籤元件
label = tk.Label(root, text="點擊確認顯示自訂圖形", padx=20, pady=20)
label.pack()

# 添加確認按鈕元件，點擊後呼叫 click1 函式顯示彈跳視窗
button = tk.Button(root, text="確認", command=click1)
button.pack()

# 啟動主迴圈
root.mainloop()
