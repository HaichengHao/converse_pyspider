"""
@File    :01aes加密utf8字节处理.py
@Editor  : 百年
@Date    :2025/4/16 19:36 
"""
# 需要pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
#
# SALT = '9cafa6466a028bfb'
# KEY = 'fd6b639dbcff0c2a1b03b389ec763c4b'
# IV = '77b07a672d57d64c'
# print(len(KEY))

def aes_encrypt(data_string):
    key_string = "fd6b639dbcff0c2a1b03b389ec763c4b"
    key = key_string.encode('utf-8')

    IV = "77b07a672d57d64c"
    iv = IV.encode('utf-8')

    data = data_string.encode('utf-8')
    aes = AES.new(
        # key=KEY.encode('utf-8'),
        key=key,

        mode=AES.MODE_CBC,
        # iv=IV.encode('utf-8')
        iv=iv
    )
    # raw = pad(data_string.encode('utf-8'), 16)
    raw = pad(data, 16)
    return aes.encrypt(raw)


data = "AE30AFED57A22A35BC160AB1A0"
result = aes_encrypt(data)
print(result)
# b'\xfe\xb6\x9e\xc53\x8b\xaf\x81r\x97;\xd6\x0c\x9b\x95\xe7x0\xfa\xce\xc2\x1f~\xfb\xb1\xb1W\x9es\xa5\xe3\x94'