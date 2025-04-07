# @Author    : 百年
# @FileName  :hexsign.py
# @DateTime  :2025/4/7 14:27
import hmac
import hashlib
import requests
import time

def hmac_sha256(key, message):
    """
    使用HMAC-SHA256算法对给定的消息进行加密
    :param key: 密钥
    :param message: 要加密的消息
    :return: 加密后的哈希值
    """
    # 将密钥和消息转换为字节串
    key = key.encode('utf-8')
    message = message.encode('utf-8')

    # 创建HMAC对象，使用SHA256哈希算法
    hmac_obj = hmac.new(key, message, hashlib.sha256)

    # 计算哈希值
    hash_value = hmac_obj.digest()

    # 将哈希值转换为十六进制字符串
    hash_hex = hash_value.hex()

    return hash_hex


if __name__ == '__main__':
    o = hmac_sha256("XgwSnGZ1p",f"ts{int(time.time())}")
    url = "https://api.bilibili.com/bapis/bilibili.api.ticket.v1.Ticket/GenWebTicket"
    params = {
        "key_id":"ec02",
        "hexsign":o,
        "context[ts]":f"{int(time.time())}",
        "csrf": ''
    }

    headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        }
    resp = requests.post(url, params=params,headers=headers).json()
    print(resp)
    ticket =  resp['data'].get('ticket')
    created_at = resp['data'].get('created_at')
    ttl = resp['data'].get('ttl')
    bili_ticket_expires = ttl+created_at
    print(f'ticket:{ticket}\ncreated_at:{created_at}\n,bili_expires:{bili_ticket_expires}')