"""
@File    :切割脚本.py
@Editor  : 百年
@Date    :2025/4/7 21:05 
"""
import json
def qiege(data):
    # data='aid=114290472326312&cid=29265235226&part=1&lv=0&ftime=1744029555&stime=1744029557&type=3&sub_type=0&refer_url=&outer=0&statistics=%7B%22appId%22%3A100%2C%22platform%22%3A5%2C%22abtest%22%3A%22%22%2C%22version%22%3A%22%22%7D&mobi_app=web&device=web&platform=web&spmid=333.788.0.0&from_spmid=333.788.0.0&session=afc7fe8b01129556602f4e02eac88cd4&csrf='

    d_lst = data.split('&')
    print(d_lst)
    kv_dic = {}
    for item in d_lst:
        kv_dic[item.split('=')[0]]=item.split('=')[1]
    # print(kv_dic)
    # 然后将其序列化,即将字典转换为json字符串
    print(json.dumps(kv_dic,indent=4))
if __name__ == '__main__':
    data = 'start_ts=1744029557&aid=114290472326312&cid=29265235226&type=3&sub_type=0&dt=2&play_type=2&realtime=3&played_time=3&real_played_time=0&refer_url=&quality=0&video_duration=7520&last_play_progress_time=3&max_play_progress_time=3&outer=0&statistics=%7B%22appId%22%3A100%2C%22platform%22%3A5%2C%22abtest%22%3A%22%22%2C%22version%22%3A%22%22%7D&mobi_app=web&device=web&platform=web&spmid=333.788.0.0&from_spmid=333.788.0.0&session=afc7fe8b01129556602f4e02eac88cd4&extra=%7B%22player_version%22%3A%224.9.29%22%7D&csrf='
    qiege(data)