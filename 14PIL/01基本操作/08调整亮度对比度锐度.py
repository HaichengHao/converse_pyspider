"""
@File    :08调整亮度对比度锐度.py
@Editor  : 百年
@Date    :2025/6/10 10:16 
"""
from PIL import Image, ImageEnhance

img = Image.open('../example.png')

# 调整亮度
brightness = ImageEnhance.Brightness(img)
bright_img = brightness.enhance(1.5)  # 亮度增加百分之50

bright_img.save('./output/bright.png')

# 增加对比度
contrast = ImageEnhance.Contrast(img)
contrast_img = contrast.enhance(1.5)  # 对比度增加50%
contrast_img.save('./output/contrast.png')

# 增加锐度
sharpness = ImageEnhance.Sharpness(img)
sharpness_img = sharpness.enhance(2.0)  # 锐度增加100%,即两倍
sharpness_img.save('./output/sharp.png')

'''
ImageEnhance 模块提供了几种增强器类，用于调整图像的不同属性
每个增强器首先需要用图像对象初始化
enhance() 方法接受一个参数，表示增强的程度:
值为1.0表示原始图像不变
值大于1.0表示增强效果（例如1.5表示增加50%）
值小于1.0表示减弱效果（例如0.5表示减少50%）
除了上面展示的三种增强器外，还有 ImageEnhance.Color 用于调整色彩饱和度'''