"""
@File    :00初体验.py
@Editor  : 百年
@Date    :2025/6/9 9:25 
"""

from PIL import Image

img = Image.open('example.png')


#显示图片
#这玩意儿会打开图库显示,如果使用jupyter的话就会在cell的output中显示
# img.show()

#获取图片信息

print('图片格式>>',img.format)
print('图片大小',img.size) #(宽,高)
print('图片模式',img.mode) #如RGB,L等等


#保存为jpg格式
# img.save('example_foramat_jpg.jpeg')
# OSError: cannot write mode RGBA as JPEG  rgba没办法写入,之后解决

'''
图片格式>> PNG
图片大小 (889, 943)
图片模式 RGBA'''