"""
@File    :app.py
@Editor  : 百年
@Date    :2025/8/14 22:47 
"""
import uvicorn
from fastapi import FastAPI,UploadFile,File
from typing import List

app = FastAPI()
@app.post('/uloadfile')
async def file(files:List[UploadFile]=File()):
    for file in files:
        print(file.filename)
    return {
        'len':len(files)
    }




if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8099)