"""
@File    :03裁剪图像.py
@Editor  : 百年
@Date    :2025/6/9 9:48 
"""
from PIL import Image

img = Image.open('../example.png')
#注意裁剪的区域(左,上,右,下)
width,height = img.size #因为会返回一个元组保存的是宽高,所以直接让俩变量接收
crop_area = (width//4,height//4,3*width//4,3*width//4)
cropped_img = img.crop(crop_area)

cropped_img.save('./output/cropped.png')

'''
crop() 方法用于从图像中提取一个矩形区域
裁剪区域由元组 (left, upper, right, lower) 定义:
left: 左边界的x坐标
upper: 上边界的y坐标
right: 右边界的x坐标
lower: 下边界的y坐标
在示例中，我们裁剪了图像的中心部分（1/4到3/4区域）
width//4 中的 // 是整数除法，确保结果是整数'''