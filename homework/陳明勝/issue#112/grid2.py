import tkinter as tk

root = tk.Tk()
root.title('不同顏色的底色')
root.geometry('300x200')

a = tk.Label(root, text='AAA', background='#f90')
b = tk.Label(root, text='BBB', background='#09c')
c = tk.Label(root, text='CCC', background='#fc0')
d = tk.Label(root, text='DDD', background='#0c9')

a.grid(column=0, row=0)  # 放在 (0,0)
b.grid(column=1, row=0)  # 放在 (1,0)
c.grid(column=0, row=1)  # 放在 (0,1)
d.grid(column=1, row=1)  # 放在 (1,1)

root.mainloop()