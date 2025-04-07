# @Author    : 百年
# @FileName  :parseData.py
# @DateTime  :2025/4/1 19:08
import base64

import hashlib

from crypto.Cipher import AES
from crypto.Cipher.AES import new
# from cryptography.hazmat.primitives.ciphers.algorithms import AES
# from Crypto.Cipher import AES

def decode_data(text):
    # 偏移量
    decodeiv = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"

    # 秘钥
    decodekey = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
    # 先把密匙和偏移量进行md5加密 digest()是返回二进制的值
    key = hashlib.md5(decodekey.encode(encoding='utf-8')).digest()
    iv = hashlib.md5(decodeiv.encode(encoding='utf-8')).digest()
    # AES解密 CBC模式解密
    aes_en = new(key, AES.MODE_CBC, iv)
    # 将已经加密的数据放进该方法
    data_new = base64.urlsafe_b64decode(text)
    # 参数准备完毕后，进行解密
    a = aes_en.decrypt(data_new).decode('utf-8').strip()
    return a

res = decode_data('_jsUyA02rwkOJ4enKX7c4Sdm4hPbMmosJtqyVVdpmzJXBjQPm4jwIuyJpaboih_vQ0Efxi8bNY0gR2oTrn6FH1zwXMT2Q9YpzDoBJ7q9QJjQcgVdeKjmW9XBf2tgUSzNBimGqRgOBPqEjog4mAEJItQVBV44_4cpgy44R45auFGI-ra7VqLJeYXfX8z5xQXchv3FrCRNrOT58u5dxuhUDBN80131f8GF4MW6Lcc5JlQ=')
print(res)