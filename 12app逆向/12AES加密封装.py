"""
@File    :12AES加密封装.py
@Editor  : 百年
@Date    :2025/5/4 12:23 
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def enc_data_aes(key_str,iv_str,data_str):
    key_str = key_str.encode('utf-8')
    iv_str = iv_str.encode('utf-8')
    data = data_str.encode('utf-8')
    aes = AES.new(
        key=key_str,
        mode = AES.MODE_CBC,
        iv=iv_str
    )
    raw = pad(data,16)
    return aes.encrypt(raw)

if __name__ == '__main__':
    data_str = "AE30AFED57A22A35BC160AB1A0"
    key_str = "fd6b639dbcff0c2a1b03b389ec763c4b"
    iv_str = "77b07a672d57d64c"

    res = enc_data_aes(key_str=key_str,iv_str=iv_str,data_str=data_str)
    print(res)
