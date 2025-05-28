# @Author    : 百年
# @FileName  :parseData.py
# @DateTime  :2024/4/1 19:08
import base64

import hashlib

from Crypto.Cipher import AES
# from crypto.Cipher import AES
from Crypto.Cipher.AES import new
# from cryptography.hazmat.primitives.ciphers.algorithms import AES
# from Crypto.Cipher import AES

def decode_data(text):
    # 偏移量
    # decodeiv = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"

    # 秘钥
    # decodekey = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"

    decodekey ="ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
    decodeiv = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"
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

# res = decode_data('_jsUyA02rwkOJ4enKX7c4Sdm4hPbMmosJtqyVVdpmzJXBjQPm4jwIuyJpaboih_vQ0Efxi8bNY0gR2oTrn6FH1zwXMT2Q9YpzDoBJ7q9QJjQcgVdeKjmW9XBf2tgUSzNBimGqRgOBPqEjog4mAEJItQVBV44_4cpgy44R45auFGI-ra7VqLJeYXfX8z5xQXchv3FrCRNrOT58u5dxuhUDBN80131f8GF4MW6Lcc5JlQ=')
# res = decode_data('_jsUyA02rwkOJ4enKX7c4Sdm4hPbMmosJtqyVVdpmzLypmsO-h0Y4u4A_9Fj-TuA9FxGNRQ_3vxVKinIJcFbE7WpWak_L-Ed9bRqgp1kA5jh5avL_EqSUibAK1rRVO761LwhjZQ2erN3GkNN7x8nRRl86NYuGcA_QCqf5einE-eLp1SE6IqFhf3xdMLnh-Mu')
# res = decode_data('_jsUyA02rwkOJ4enKX7c4Sdm4hPbMmosJtqyVVdpmzLO1YGh3NbII8SLMj0GD9RKLli5ed8gAUGEep7cptPst7YTFqbpbCGjuqXOGLo4bF_1zVR_vNxfgXpC-ByOTdrLrH3zGzoqYDo6j9ZQGRE5kyVnCuPjxBCJ_S7lOf_mrds=')
res = decode_data('_jsUyA02rwkOJ4enKX7c4Sdm4hPbMmosJtqyVVdpmzIl22x1usTpIyBfXVREejEaidSrn-4uSyG2D5mjKYGwygo5vj1Ylh8wKj_nC-O-YvdLNAl2cxO7QK4Z4Fvg6FsswBK8SDR2XfhyA7lUeQAMZ1WCdNEouKCjg1X3D7_iOWnJTmkooilPH1U7oC2jfx8jRvrsGNwiqoQIxn00X6rDPY4fKdiXZoey2HNL0MCaVQY=')
print(res)
