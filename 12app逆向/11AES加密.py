"""
@File    :11AES加密.py
@Editor  : 百年
@Date    :2025/5/4 10:15 
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key_string = "fd6b639dbcff0c2a1b03b389ec763c4b"
key = key_string.encode('utf-8')

IV = "77b07a672d57d64c"
iv = IV.encode('utf-8')

data_string = "AE30AFED57A22A35BC160AB1A0"
data = data_string.encode('utf-8')

aes = AES.new(
    key=key,
    iv=iv,
    mode=AES.MODE_CBC
)

raw = pad(data,16)
print(raw)

