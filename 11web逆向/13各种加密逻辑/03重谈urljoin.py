"""
@File    :03重谈urljoin.py
@Editor  : 百年
@Date    :2025/5/30 10:25 
"""
from urllib.parse import urljoin

base_url = 'https://www.xxx.com/q/a/b'

s1 = 'c/d/index.html'
print(urljoin(base_url,s1))

# https://www.xxx.com/q/a/c/d/index.html <--相当于在当前文件夹a下面找c文件夹下的d文件夹中的index.html
s2 = '/c/d/index.html'

print(urljoin(base_url,s2))
# https://www.xxx.com/c/d/index.html <--相当于在根目录中找c文件夹下的d文件夹下的index.html

