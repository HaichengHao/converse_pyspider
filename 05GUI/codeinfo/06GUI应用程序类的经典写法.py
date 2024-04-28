# @Editor    : 百年
# @FileName  :06GUI应用程序类的经典写法.py
# @Time      :2024/4/24 21:47
from tkinter import *
from tkinter import messagebox

base_window = Tk()
base_window.title("GUI程序的经典写法")

base_window.geometry("500x400+200+200")
btn1 = Button(base_window)
btn1["text"] = "按钮1"

btn1.pack()

def btn1_func(e):
    messagebox.showinfo("窗口2的标题","人就是这样，永远有一颗好奇心")

btn1.bind("<Button-1>", btn1_func)

base_window.mainloop()