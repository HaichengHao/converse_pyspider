"""
@File    :07应用滤镜.py
@Editor  : 百年
@Date    :2025/6/10 10:07 
"""
from PIL import Image, ImageFilter

img = Image.open('../example.png')

# 模糊滤镜
blurred_img = img.filter(ImageFilter.BLUR)
blurred_img.save('./output/blureddog.png')

# 边缘增强
edge_img = img.filter(ImageFilter.EDGE_ENHANCE)
edge_img.save('./output/edgeenhance.png')

# 轮廓滤镜
contour_img = img.filter(ImageFilter.CONTOUR)
contour_img.save('./output/contour.png')


'''
filter() 方法用于对图像应用各种预定义的滤镜效果
ImageFilter.BLUR 会使图像模糊，类似于柔焦效果
ImageFilter.EDGE_ENHANCE 增强图像的边缘，使轮廓更明显
ImageFilter.CONTOUR 寻找图像的轮廓线，产生类似素描的效果
其他常用滤镜还有:
ImageFilter.SHARPEN: 锐化图像
ImageFilter.EMBOSS: 浮雕效果
ImageFilter.FIND_EDGES: 寻找边缘
ImageFilter.SMOOTH: 平滑图像
也可以创建自定义滤镜，
如高斯模糊: img.filter(ImageFilter.GaussianBlur(radius=2))'''