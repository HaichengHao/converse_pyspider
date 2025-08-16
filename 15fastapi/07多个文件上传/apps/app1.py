"""
@File    :app1.py
@Editor  : 百年
@Date    :2025/8/14 21:44 
"""

'''
多个文件上传只需要将bytes修改为被List对象包含即可'''

from fastapi import APIRouter, File
from typing import List

filedemo = APIRouter(prefix='/fileupload')


@filedemo.post('/')
async def get_file(files: List[bytes] = File()):  # important:文件是字节流,所以类型应该是bytes,并且默认应该是File对象
    for idx,file in enumerate(files):
        print("filename",files)
        with open(f'./demo{idx}.png','wb') as f:
            f.write(file)
    return {
        "length":len(files)
    }
