# @Editor    : 百年
# @FileName  :04GUI编程整体描述.py
# @Time      :2024/4/24 17:14
'''
图形用户界面是由一个个组件组成，就像小孩“搭积木”一样最终组成了整个界面。
有的组件还能在里面再放置其他组件，我们称为“容器”。
主要的关系
#todo:见others文件的Tkinter中GUI组件的关系图
# 想要查看Diagrams只需要右键点击show diagrams即可
'''

from tkinter import *
from tkinter import messagebox

basewindow = Tk() #创建底层框架

basewindow.title('我的GUI')
basewindow.geometry('500x400+400+400') #定义位置，界面画幅500x400距左边400像素，距上边400像素

btn1 = Button(basewindow) #创建btn1对象，是一个按钮，在基底上
btn1["text"] = "我是按钮1"
btn1.pack() #打包按钮

def btn1_func(e):
    messagebox.showinfo("Message","点我，我就给你跳出窗口")

# 绑定事件
btn1.bind("<Button-1>", btn1_func)

# 调用.mainloop()进行循环的可视化
basewindow.mainloop()