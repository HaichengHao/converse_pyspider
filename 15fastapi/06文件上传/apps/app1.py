"""
@File    :app1.py
@Editor  : 百年
@Date    :2025/8/14 21:44 
"""
from fastapi import APIRouter, File

filedemo = APIRouter(prefix='/fileupload')


@filedemo.post('/')
async def get_file(file: bytes = File()):  # important:文件是字节流,所以类型应该是bytes,并且默认应该是File对象
    print("file",file)
    with open('./demo.png','wb') as f:
        f.write(file)
    return {
        'filename':'demo.png',
        'bytes_len':len(file)
    }
