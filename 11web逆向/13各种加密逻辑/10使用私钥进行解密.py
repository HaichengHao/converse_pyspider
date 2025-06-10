"""
@File    :10使用私钥进行解密.py
@Editor  : 百年
@Date    :2025/6/2 10:23 
"""
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

#密文
miwen = 'FfXEjq4Uy3zikwtTMVw+q9HqmhSyoMkUjI/VaA/JrKkp/gdLgqlKCg+0s+dttvtlDKdLE2L+WD0hseEFXhSo7hVo3aQyevtzOAokZY0ZM5Anq+hQSt4EyBxnco7ABe3iCYTJuUEqWIw0bnUB+Fq9tRshDwKsBwNCKQ2TBjM8QSUmcGa9Zvy/pdY4sPM9FGKe3vYcsejnmAbnp3llIcquSjO+clUrCI9/4HDB2bB5yxw4trxVtDukxtMWYZgyYDBvW1waL6i70h9F7/blTNSJiE5GSfktENHXY1tQsQuSpQx9N7N8sLLpIDMmmFfqv122GPncbA1zz7eoGU/Vncopkg=='

#step1:因为是base64字符串,先将其转换为字节
b_s = base64.b64decode(miwen)
print(b_s)

#构建解密器,对其进行解密
#step2:读取自己的私钥,但其实我们一般不考虑解密的事情,这是交给服务器端的

pri_k = RSA.import_key(open('private.pem','rb').read())
# pri_k = RSA.import_key(k) 或者直接写的话就导入字节格式的密钥
rsa = PKCS1_v1_5.new(key=pri_k)
s = rsa.decrypt(b_s,sentinel='None') #important:注意这里要求要有一个位置参数表示报错后该参数执行,是规定,虽然用不到但是也要强制指定
print(s)
# b'hello,\xe6\x88\x91\xe5\x8f\xabhero,\xe4\xbd\xa0\xe6\x98\xaf??'

#step3:还原
print(s.decode()) #tips:因为默认是utf-8,这里就不指定了
# hello,我叫hero,你是??
