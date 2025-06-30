"""
@File    :get_index_data.py
@Editor  : 百年
@Date    :2025/6/23 20:43 
"""
from flask import session
from myweb_optimize.utils import dbhelper
from datetime import datetime


def get_index_data(per_page_count, offset):
    uid = session['user_info'][0]['ID']
    item = dbhelper.show_info(uid, per_page_count=per_page_count, offset=offset)  # 推荐按 uid 查询当前用户的数据
    processed_data = [list(d.values())[2] for d in item]  # 通过这个拿到状态码
    datanum = dbhelper.get_count(uid).get('count(*)')  # 获取数据的总条数

    pagesize = 5
    total_pages = (datanum + pagesize - 1) // pagesize
    print(total_pages)
    return {
        'msg': session['user_info'],
        'item': item,
        'time': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'datanum': datanum,
        'total_pages': total_pages,
        'processed_data': processed_data
    }
