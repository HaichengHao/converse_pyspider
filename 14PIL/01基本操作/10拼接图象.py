"""
@File    :10拼接图象.py
@Editor  : 百年
@Date    :2025/6/10 13:09 
"""
from PIL import Image
img = Image.open(
    '../example.png'
)
width,height = img.size

#创建灰度图
gray_scaleimg = img.convert('L')

#创建一个新的图像,宽度是原图的两倍,高度相同
merged_img = Image.new('RGB',(width*2,height))

#将原图放在右边
merged_img.paste(img,(0,0))
#将灰度图放在左边
merged_img.paste(gray_scaleimg,(width,0))
merged_img.save('./output/mergedimg.png')