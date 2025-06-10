"""
@File    :01调整图像大小.py
@Editor  : 百年
@Date    :2025/6/9 9:45 
"""
from PIL import Image
img = Image.open('../example.png')
resized_img = img.resize((400,300))
resized_img.save('./output/resized.png')


'''

resize() 方法用于改变图像尺寸，参数是一个包含新宽度和高度的元组
这个方法不会修改原始图像，而是返回一个新的图像对象
默认情况下使用最近邻插值法，对于更高质量的调整可以添加参数：resized_img = img.resize((400, 300), Image.LANCZOS)
save() 方法将处理后的图像保存到指定路径
'''