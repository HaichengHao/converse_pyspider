# @Editor    : 百年
# @FileName  :01初识gui.py
# @Time      :2024/4/24 16:03
'''
GUI（Graphics User Interface），
即图形用户界面编程，我们可以通过 python 提供的丰富的
组件，快速的实现使用图形界面和用户交互。GUI 编程类似于“搭积木”，
将一个个组件(Widget)放到窗口中。
'''
# 基于 tkinter 模块创建 GUI 程序包含如下4 个核心步骤：

# 1. 创建应用程序主窗口对象（也称：根窗口）
# (1) 通过类 Tk 的无参构造函数
from tkinter import *
from tkinter import messagebox
root = Tk()

# 2. 在主窗口中，添加各种可视化组件，比如：按钮（Button）、文本框（Label）等。
btn01 = Button(root)
btn01["text"] = "点我就撒花"

# 3. 通过几何布局管理器，管理组件的大小和位置
btn01.pack()


# 4. 事件处理
# (1) 通过绑定事件处理程序，响应用户操作所触发的事件（比如：单击、双击等）

# def songhua(e):
#     messagebox.showinfo("Message", "送你一朵玫瑰花，请你爱上我")
# print("送你 99 朵玫瑰花")
# btn01.bind("<Button-1>", songhua)
