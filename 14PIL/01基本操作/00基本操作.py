"""
@File    :00基本操作.py
@Editor  : 百年
@Date    :2025/6/9 9:39 
"""
from PIL import Image,ImageFilter,ImageEnhance,ImageDraw,ImageFont
import os

def main():
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    #打开图像并显示图像的基本信息
    try:
        img = Image.open('../example.png')
        print(f'图像信息如下:-格式{img.format},-大小{img.size},-模式{img.mode}')
    except Exception as e:
        print(f'图像无法打开,{e}')
if __name__ == '__main__':
    main()

'''
Image.open() 函数用于打开图像文件，参数是图像文件的路径
img.format 显示图像的格式（如JPEG, PNG, GIF等）
img.size 返回一个包含宽度和高度的元组，如(800, 600)
img.mode 显示图像的颜色模式:
RGB: 彩色图像
RGBA: 带透明通道的彩色图像
L: 灰度图像
1: 二值图像（黑白）


'''