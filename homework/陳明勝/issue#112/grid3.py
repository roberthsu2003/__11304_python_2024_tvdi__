import tkinter as tk

root = tk.Tk()
root.title('不同顏色的底色')
root.geometry('500x200')

frame = tk.Frame(root)
frame.pack()

a = tk.Label(frame, text='AAA', background='#f90')
b = tk.Label(frame, text='BBB', background='#09c')
c = tk.Label(frame, text='CCC', background='#fc0')
d = tk.Label(frame, text='DDD', background='#0c9')


a.grid(column=0, row=0)
b.grid(column=1, row=0)
c.grid(column=0, row=1)
d.grid(column=1, row=1)

e = tk.Label(root, text='EEE', background='#ccc')
e.pack(fill='x')

root.mainloop()