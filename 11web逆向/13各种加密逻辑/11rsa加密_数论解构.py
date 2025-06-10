"""
@File    :11rsa加密_数论解构.py
@Editor  : 百年
@Date    :2025/6/4 15:16 
"""

'''
具体描述如下

1.任意选取两个不同的大素数p和q计算乘积n=pq,phi(n)=(p-1)(q-1)  

2.任意选取一个大整数e，满足e与phi(n)的最大公约数等于1，整数e用做加密钥（注意：e的选取是很容易的，例如，所有大于p和q的素数都可用）

3.确定的解密钥d，满足 d*e % phi(n)=1，即d*e = k*phi(n)+1,k>=1 是一个任意的整数；所以，若知道e和phi(n)，则很容易计算出d

4.公开整数n和e(即公钥)，秘密保存d(即私钥)

5.将明文m（m<n是一个整数）加密成密文c，加密算法为
    c = E(m) = m^e % n
    
6.将密文c解密为明文m，解密算法为
    m = D(c) = c^d % n
    
然而只根据n和e（注意：不是p和q）要计算出d是不可能的。
因此，任何人都可对明文进行加密，但只有授权用户（知道d）才可对密文解密
'''

#实现
p = 7
q = 13

n = p*q
print(f'n={n}')


#求欧拉数
phi_n = (p-1)*(q-1)
print(f'phi_n={phi_n}')

#随便找一个质数满足e和phi_n的最大公约数是1
e = 43


#确定d
# for d in range(1,phi_n):
#     if d*e %phi_n==1:
#         print(d)


#封装
def getd(phi_n):
    for d in range(1, phi_n):
        if d * e % phi_n == 1:
            return d
            print(d)
            break
#调用自己的方法去获取d,然后进行下一步的计算
d = getd(phi_n=phi_n)
print(f'd={d}')

#然后进入下一步的加密逻辑

#定义明文m ,m是小于n的
m = 18
print(f'明文m={m}')
# 进行加密
c =m**e % n
print(f'c={c}')

#然后进行解密
m_jiemi  = c**d % n
print(f'解密后的明文{m_jiemi}')

#复现完毕

'''
实际的解密过程之中,主要需要关注的就是e和n
如果遇到js里有rsakeypair,那么就需要找到key和n来对其进行复现'''


'''
当乐网解构
var rsa = function (arg) {
      setMaxDigits(130);
      var PublicExponent = "10001";  这个就是e
      下面这个就是16进制的n
      var modulus = "be44aec4d73408f6b60e6fe9e3dc55d0e1dc53a1e171e071b547e2e8e0b7da01c56e8c9bcf0521568eb111adccef4e40124b76e33e7ad75607c227af8f8e0b759c30ef283be8ab17a84b19a051df5f94c07e6e7be5f77866376322aac944f45f3ab532bb6efc70c1efa524d821d16cafb580c5a901f0defddea3692a4e68e6cd";
      var key = new RSAKeyPair(PublicExponent, "", modulus);
      return encryptedString(key, arg);
  };
  
'''