"""
@File    :02.py
@Editor  : 百年
@Date    :2025/6/9 22:46 
"""
from PIL import Image

img = Image.open('../example.png')
#显示图像的基本信息
print(f'图像的格式{img.format}')
print(f'图像大小(width*height){img.size}')
print(f'图像模式{img.mode}')