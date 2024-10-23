# @Editor    : 百年
# @FileName  :03主窗口的大小和位置.py
# @Time      :2024/4/24 16:48

# 讲解窗口的位置及大小
'''
tkinter 主窗口
主窗口位置和大小
通过 .geometry(‘wxh±x±y’)进行设置。
w为宽度，h为高度。
+x 表示距屏幕左边的距离；-x 表示距屏幕右边的距离；
+y表示距屏幕上边的距离；-y 表示距屏幕下边的距离。
'''
from tkinter import *
from tkinter import messagebox

root = Tk()  # 创建窗口对象，Tk()创建根窗口
root.title('my_GUI_APP') #框架起个名字
root.geometry('500x500+300+300') #定义一个窗口，画幅500x500像素，举例左边300像素，举例上边300像素
# 创建按钮对象
btn01 = Button(root)  # 把创建的Button对象放到窗口root中去
btn02 = Button(root)  # 创建第二个按钮
# 给按钮命名
btn01["text"] = "点我送花"  # 定义第一个按钮的名称
btn02["text"] = "点我送钱"  # 定义第二个按钮的名称
# 对按钮进行打包
btn01.pack()  # 按钮设置完毕后调用布局管理器功能，即.pack()
btn02.pack()



# 定义一个事件,点击按钮会弹出窗口，注意，需要导入messagebox
def songhua(e):  # e就是事件对象
    messagebox.showinfo("Message", "送你一朵花")  # 界面显示
    print("hello")  # 控制台显示


def songqian(e):
    messagebox.showinfo("Message", "送钱啦")
    print("hello")  # 控制台显示


# 事件定义完毕后需要对事件进行绑定
# 对点击按钮会发生的事件进行绑定
btn01.bind("<Button-1>", func=songhua)  # 左键单击会调用songhua()
btn02.bind("<Button-1>", func=songqian)  # 左键单击会调用songqian()

# 可视操作
root.mainloop()  # .mainloop()方法，进入事件循环
