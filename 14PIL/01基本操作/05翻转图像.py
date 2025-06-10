"""
@File    :05.py
@Editor  : 百年
@Date    :2025/6/9 23:01 
"""
from PIL import Image
img = Image.open('../example.png')

# 水平翻转
h_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
h_flipped.save('./output/h_flipped.png')

#垂直翻转
v_flipped = img.transpose(Image.FLIP_TOP_BOTTOM)
v_flipped.save('./output/v_flipped.png')

'''
transpose() 方法用于图像的翻转和转置操作
Image.FLIP_LEFT_RIGHT 常量表示水平翻转（左右镜像）
Image.FLIP_TOP_BOTTOM 常量表示垂直翻转（上下镜像）
除了翻转，还可以使用其他常量如 Image.ROTATE_90, 
Image.ROTATE_180, Image.ROTATE_270 进行旋转'''