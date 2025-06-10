"""
@File    :04旋转图像.py
@Editor  : 百年
@Date    :2025/6/9 22:50 
"""
from PIL import Image
img = Image.open('../example.png')

rotated_img = img.rotate(45,expand=True) #旋转45度,expand=True保留整个图像
rotated_img.save('./output/rotated.png')

'''
rotate() 方法用于旋转图像，第一个参数是旋转角度（逆时针，以度为单位）
expand=True 参数会扩展输出图像的尺寸，以容纳整个旋转后的图像
如果不设置 expand=True，旋转后的图像会被裁剪以适应原始尺寸
默认情况下，旋转中心是图像的中心点'''