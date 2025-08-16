"""
@File    :02路径参数.py
@Editor  : 百年
@Date    :2025/7/30 20:38 
"""
from fastapi import FastAPI,templating
import uvicorn
app = FastAPI()

@app.get('/items/{item_id}') #tips:在这种情况下，item_id 被声明为 int 类型。
# tips:这里可以发现flask与fastapi对于参数类型处理的不同之处,fastapi是写在路由函数的参数中,
#  而flask则是会在路由中使用<类型:名称> 这样来定义
async def getid(item_id: int): #tips:指定其属于int类
    return {'item_id':item_id}

#在创建路径操作时，你可能会遇到固定路径的情况
'''
比如 /users/me，假设它是用于获取当前用户的数据。

然后你也可以有一个路径 /users/{user_id}，用于通过某个用户 ID 获取特定用户的数据。

因为路径操作是按顺序评估的，所以你需要确保 /users/me 的路径在 /users/{user_id} 之前声明
'''

@app.get('/users/me')
async def read_user_me():
    return {"user_id":"the current user"}

@app.get('/users/{user_id}')
async def read_user(user_id:str): #tips:指定其属于str类
    return {'user_id':user_id}
#tips: 否则，/users/{user_id} 的路径也会匹配 /users/me，并“认为”它接收到的参数 user_id 的值是 "me"。


# 同样，你不能重新定义路径操作
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

# 第一个将始终被使用，因为路径首先匹配。

# important:如果你有一个接收路径参数的路径操作，但你希望可能的有效路径参数值是预定义的，你可以使用标准的 Python Enum


'''
创建一个 Enum 类¶
导入 Enum 并创建一个继承自 str 和 Enum 的子类。

通过继承 str，API 文档将能够知道这些值必须是 string 类型，并能够正确渲染。

然后创建具有固定值的类属性，这些属性将是可用的有效值
'''

# step1
from enum import Enum

class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
# step2
'''
声明一个路径参数¶
然后使用你创建的枚举类（ModelName）作为类型注解，创建一个路径参数'''

#important:参数中可以写接口的一些信息

@app.get("/models/{model_name}",tags=['深度学习的几个网络'],summary="这是一个概述内容",\
         description="这是一个详情内容",\
         response_description="这是响应的描述！！！",\
         deprecated=True)
async def getmodel(model_name:ModelName):#tips:指定其属于我们自定义的类
    # tips:你可以将其与你创建的枚举 ModelName 中的枚举成员进行比较
    if model_name is ModelName.alexnet:
        return {'model_name':model_name,"message":"Deep Learning FTW"}
    # tips:你可以使用 model_name.value 获取实际值（在本例中为 str），或者通常使用 your_enum_member.value
    if model_name.value == 'lenet':
        return {'model_name':model_name,"message":"leCNN all the images"}
    return {'model_name':model_name,"message":"Have some residuals"}

'''
包含路径的路径参数¶
假设你有一个路径操作，其路径为 /files/{file_path}。

但是你需要 file_path 本身包含一个路径，例如 home/johndoe/myfile.txt。

所以，该文件的 URL 将类似于：/files/home/johndoe/myfile.txt。

OpenAPI 支持¶
OpenAPI 不支持声明一个路径参数包含路径的方式，因为这可能导致难以测试和定义的场景。

然而，你仍然可以在 FastAPI 中使用 Starlette 的一个内部工具来实现它。

并且文档仍然有效，尽管不会添加任何说明该参数应包含路径的文档。

路径转换器¶
通过直接使用 Starlette 的一个选项，你可以使用如下 URL 声明一个包含路径的路径参数：
'''
# /files/{file_path:path}

# 在这种情况下，参数的名称是 file_path，最后一部分 :path 告诉它该参数应该匹配任何路径。
#
# 所以，你可以这样使用它：

@app.get("files/{file_path:path}") #tips:注意这里和flask的很像
async def read_file(file_path:str):
    return {"file_path":file_path}

# summary:总结¶
#  使用 FastAPI，通过使用简短、直观和标准的 Python 类型声明，你将获得：
#  编辑器支持：错误检查、自动补全等。
#  数据“解析”
#  数据验证
#  API 注解和自动文档
#  并且你只需要声明一次。
#  这可能是 FastAPI 相对于其他框架的主要显著优势（除了原始性能）。

if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8099)