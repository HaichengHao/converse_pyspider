"""
@File    :09添加文字.py
@Editor  : 百年
@Date    :2025/6/10 10:31 
"""
from PIL import Image,ImageDraw,ImageFont

img = Image.open('../example.png')

# 创建一个副本用于绘制
img_copy = img.copy()
draw = ImageDraw.Draw(img_copy)
## 尝试使用系统字体，如果失败则使用默认
try:
    font = ImageFont.truetype('arial.ttf',50) #指定字体像素为50
except IOError:
    font = ImageFont.load_default()

#在图片上添加文字 fill指定的是颜色,rgb
draw.text((img_copy.width//2,img_copy.height//2),"DOG",fill=(255,120,120),font=font)
img_copy.save('./output/text_img.png')

'''
copy() 方法创建原图像的一个副本，避免修改原始图像
ImageDraw.Draw() 创建一个绘图对象，用于在图像上绘制
ImageFont.truetype() 用于加载TrueType字体:
第一个参数是字体文件路径（如"arial.ttf"）
第二个参数是字体大小（以像素为单位）
draw.text() 用于在图像上绘制文字:
第一个参数 (10, 10) 是文字的位置坐标（左上角）
第二个参数是要绘制的文本内容
fill 参数指定文字颜色，这里是白色 (255, 255, 255)
font 参数指定使用的字体
使用 try-except 块处理可能的字体加载失败情况'''
