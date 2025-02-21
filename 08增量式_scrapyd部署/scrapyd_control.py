"""
@File    :scrapyd_control.py
@Editor  : 百年
@Date    :2025/2/21 13:11 
"""

# abst: 使用requests模块控制scrapy项目,前提是你已经scrapyd-deploy 部署名 -p 项目名
import requests
print('控制选项:\t\t\n1.启动爬虫\n2.关闭爬虫\n3.删除爬虫\n0.退出操作\n'
      '注意关注localhost:6800查看你是否正确开启部署项目\n'
      '如果未部署,请先scrapyd-deploy 部署名 -p 项目名【可先查看scrapy.cfg】')

optnumber = int(input('请输入操作码>>'))
while 1:
    if optnumber == 0:
        print('退出成功!!')
        break
    if optnumber == 1:
        #important:我将会新写一份，这份太简陋
        # 启动爬虫
        url = 'http://localhost:6800/schedule.json'
        project = input('请输入项目名>>')
        spider = input('请输入爬虫名称>>>')
        data = {
            'project':f'{project}',
            'spider': f'{spider}',
        }
        resp = requests.post(url, data=data)
        print('开启成功，请关注下列信息>>\n',resp.json())
        break
    elif optnumber == 2:
        # 停止爬虫
        jobid=input('请输入您要关闭的jobid>>')
        url = 'http://localhost:6800/cancel.json'
        data = {
            'project': 'zlsDEMO2',
            'job':f'{jobid}',
        }
        resp = requests.post(url, data=data)
        print('job终止成功',resp.json())
        break
    elif optnumber == 3:
        project = input('请输入项目名称>>>')
        url = 'curl http://localhost:6800/delproject.json'
        data = {
            'project': f'{project}',
        }
        resp = requests.post(url, data=data)
        print('项目删除操作成功',resp.json())
        break
    else:
        print('您的输入信息有误，请重新输入')
        break