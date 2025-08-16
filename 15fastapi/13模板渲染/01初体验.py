"""
@File    :01初体验.py
@Editor  : 百年
@Date    :2025/8/15 17:07 
"""


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

#step1:挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

#step2:再定义模板文件,注意，利用的是Jinja2Templates的方法
templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse) #step3:返回类型要是HTMLResponse类型
async def read_item(request: Request, id: str):
    return templates.TemplateResponse( #step4:指定返回的模板html以及携带的jinja占位数据
        request=request, name="item.html", context={"id": id}
    )