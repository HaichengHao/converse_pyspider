"""
@File    :11保存为不同格式.py
@Editor  : 百年
@Date    :2025/6/10 13:16 
"""
from PIL import Image

img = Image.open('../example.png')

# 将图像保存为不同的格式
img.save('./output/example_vjpg.jpg')

# 保存为JPEG,设置质量
img.save('./output/highq.png', quality=95)  # 高质量
img.save('./output/lowq.png', quality=10)


'''
save() 方法根据文件扩展名自动确定保存格式
不同格式的特点:
PNG: 无损压缩，支持透明度，适合图标、截图等
JPEG: 有损压缩，适合照片，不支持透明度
BMP: 无压缩，文件较大，但保留所有信息
GIF: 支持动画，最多256色
对于JPEG格式，可以通过 quality 参数控制压缩质量:
值范围从1（最差质量，最小文件）到95（最佳质量，较大文件）
默认值通常为75
不同质量设置可以帮助平衡图像质量和文件大小'''