"""
@File    :06.py
@Editor  : 百年
@Date    :2025/6/10 10:02 
"""
from PIL import Image
img = Image.open('../example.png')

#转换颜色模式
grayscale_img = img.convert('L')  #转换为灰度图
grayscale_img.save('./output/grayscale_dog.png')

'''
convert() 方法用于更改图像的模式（颜色空间）
参数 'L' 表示转换为灰度图像（Luminance）
其他常用的模式包括:
'RGB': 三通道彩色
'RGBA': 四通道彩色（带透明度）
'CMYK': 印刷四色模式
'1': 二值图像（纯黑白）
转换模式可以减小文件大小或为特定处理做准备'''