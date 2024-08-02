import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO
from PIL import Image, ImageTk
from tkinter import Toplevel, Frame, Label
import tkinter as tk
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def plot_missing_values(data):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axis('off')  # 隱藏圖表

    # 獲取缺失值資訊並轉換為文本
    buf = StringIO()
    data.info(buf=buf)
    info_str = buf.getvalue()

    # 在圖表上顯示缺失值資訊
    ax.text(0.5, 0.5, info_str, fontsize=12, ha='center', va='center', wrap=True)
    plt.title('Missing Values Check')

    # 將圖表轉換為 PIL Image
    canvas = FigureCanvas(fig)
    canvas.draw()
    pil_image = Image.frombytes('RGBA', canvas.get_width_height(), canvas.buffer_rgba())

    # 調整圖片大小
    pil_image = pil_image.resize((400, 350), Image.LANCZOS)

    plt.close(fig)  # 關閉圖表，釋放資源
    return pil_image

def plot_boxplot(data):
    # 求出四分位距(IQR)=Q3-Q1與上邊界(天花板)和下邊界(地板)，並輸出資料到終端機
    # Q1 = data['PRICE'].quantile(0.25)
    # Q3 = data['PRICE'].quantile(0.75)
    # IQR = Q3 - Q1
    # Upper = Q3 + 1.5 * IQR
    # Lower = Q1 - 1.5 * IQR
    # print('Summary statistics:')
    # print('Q3=', Q3, 'Q1=', Q1, 'IQR=', IQR, 'Upper=', Upper, 'Lower=', Lower)

    # 創建圖表並繪製盒鬚圖
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.boxplot(data['PRICE'], showmeans=True)
    ax.set_title('Boxplot of Price')
    ax.set_ylabel('Price')

    # 將圖表轉換為 PIL Image
    canvas = FigureCanvas(fig)
    canvas.draw()
    pil_image = Image.frombytes('RGBA', canvas.get_width_height(), canvas.buffer_rgba())

    # 調整圖片大小
    pil_image = pil_image.resize((400, 350), Image.LANCZOS)

    plt.close(fig)  # 關閉圖表，釋放資源
    return pil_image

def plot_normal_distribution(data):
    # 創建圖表並繪製常態分佈圖
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(data['PRICE'], kde=True, ax=ax)
    ax.set_title('Normal Distribution of Price')
    ax.set_xlabel('Price')
    ax.set_ylabel('Frequency')

    # 將圖表轉換為 PIL Image
    canvas = FigureCanvas(fig)
    canvas.draw()
    pil_image = Image.frombytes('RGBA', canvas.get_width_height(), canvas.buffer_rgba())

    # 調整圖片大小
    pil_image = pil_image.resize((400, 350), Image.LANCZOS)

    plt.close(fig)  # 關閉圖表，釋放資源
    return pil_image

def show_plots_in_window(window):
    script_dir = os.path.dirname(__file__)
    relative_path = os.path.join('..', 'train_dataset.csv')
    dataset_path = os.path.abspath(os.path.join(script_dir, relative_path))

    try:
        data = pd.read_csv(dataset_path)
        print("成功載入資料1")
    except FileNotFoundError:
        print(f"找不到檔案: {dataset_path}")
        return
    except Exception as e:
        print(f"發生錯誤: {e}")
        return

    frame = Frame(window, bg="white")
    frame.pack(fill="both", expand=True)

    for widget in frame.winfo_children():
        widget.destroy()

    chart_frame = Frame(frame, bg="white")
    chart_frame.pack(side=tk.TOP, padx=5, pady=5)

    # 顯示缺失值圖表
    missing_values_image = plot_missing_values(data)
    missing_values_photo = ImageTk.PhotoImage(image=missing_values_image)
    label_missing_values = Label(chart_frame, image=missing_values_photo)
    label_missing_values.pack(side=tk.LEFT, padx=5, pady=5)

    # 顯示盒鬚圖
    boxplot_image = plot_boxplot(data)
    boxplot_photo = ImageTk.PhotoImage(image=boxplot_image)
    label_boxplot = Label(chart_frame, image=boxplot_photo)
    label_boxplot.pack(side=tk.LEFT, padx=5, pady=5)

    # 顯示常態分佈圖
    normal_dist_image = plot_normal_distribution(data)
    normal_dist_photo = ImageTk.PhotoImage(image=normal_dist_image)
    label_normal_distribution = Label(chart_frame, image=normal_dist_photo)
    label_normal_distribution.pack(side=tk.LEFT, padx=5, pady=5)

    # 保持圖片引用，防止被垃圾回收
    chart_frame.image = (missing_values_photo, boxplot_photo, normal_dist_photo)
