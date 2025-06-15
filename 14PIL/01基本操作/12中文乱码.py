"""
@File    :12中文乱码.py
@Editor  : 百年
@Date    :2025/6/11 9:26 
"""

from PIL import Image,ImageDraw,ImageFont

img = Image.new('RGB',(400,200),color=(255,0,0))

#创建imageDraw 图像
draw = ImageDraw.Draw(img)
#
# #指定字体为默认字体
# font = ImageFont.load_default()
# #注意默认字体可能不支持中文
#
# draw.text((200,100),"hello,pillow",fill='black',font=font,font_size=20) #指定填充色为黑色
#
# #保存图像,质量为85
# img.save('./output/demo.jpeg',quality=85)


'''
默认情况下，Pillow 的默认字体不支持中文显示。

要在图像上添加中文，我们需要使用支持中文的字体文件（通常是 .ttf 或 .otf 格式）。
可以从以下途径获取中文字体：

使用系统自带的中文字体（如 Windows 的 simsun.ttc）

从免费字体网站下载（如思源黑体、阿里巴巴普惠体等）。

购买商业字体（注意版权问题）
开源的中文字体库下载：https://github.com/wordshub/free-font。
'''

#tips:指定中文字体
font_path = "C:\Windows\Fonts\simhei.ttf"
font_size = 20

font = ImageFont.truetype(font_path,font_size)

#添加中文文字
draw.text((20,20),'你好啊,pillow',fill='yellow',font=font)

img.save('./output/chinese_font.png')
