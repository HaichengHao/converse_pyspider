"""
@File    :wymusic.py
@Editor  : 百年
@Date    :2025/5/24 15:41 
"""
'''
https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=77ddf93cdc2cda59db3e088d3c2e38b6

                    /api/song/enhance/player/url/v1
encodeType: "aac"  音乐解码方式
ids: "[307606]" 音乐id
level: "exhigh"  音质

params    经过两次aes加密得到
encSecKey 经过一次rsa加密得到


npm i rypto-js
'''
