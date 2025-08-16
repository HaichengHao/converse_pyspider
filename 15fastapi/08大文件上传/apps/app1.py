"""
@File    : app1.py
@Editor  : 百年
@Date    : 2025/8/14 21:44
"""
import os
from fastapi import APIRouter, File, UploadFile
from typing import List

filedemo = APIRouter(prefix='/fileupload')

@filedemo.post('/')
async def get_file(file: UploadFile):
    # 1. 确保目录存在
    upload_dir = "./imgs"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)  # makedirs 可以创建多级目录

    # 2. 构造文件保存路径
    file_path = os.path.join(upload_dir, file.filename)

    # 3. 读取上传的文件内容（bytes），并写入目标路径
    contents = await file.read()  # 读取为 bytes
    with open(file_path, 'wb') as f:
        f.write(contents)

    return {
        'filename': file.filename,
        'filesize': file.size,
        'content_type': file.content_type
    }