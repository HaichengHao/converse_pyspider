"""
@File    :算法还原.py
@Editor  : 百年
@Date    :2025/6/4 10:19 
"""
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

#公钥的b64字符串
b64s = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDhNhuAr4UjFv+cj99PbAQWWx9H \
X+3jSRThJqJdXkWUMFMTRay8EYRtPFIiwiOUU4gCh4ePMxiuZJWUBHe1waOkXEFc \
Kg17luhVqECsO+EOLhxa3yHoXA5HcSKlG85hNV3G4uQCr+C8SOE0vCGTnMdnEGmU \
nG1AGGe44YKy6XR4VwIDAQAB"

#要将其转换为字节,然后才能加载为公钥
b64 = base64.b64decode(b64s)
# print(b64)
pubk = RSA.import_key(b64)
rsa = PKCS1_v1_5.new(key=pubk)

res = rsa.encrypt('123456'.encode('utf-8'))
print(res)

#然后将这一堆转换为b64字符串
resfinal = base64.b64encode(res).decode('utf-8')
print(resfinal)
