"""
@File    :03对照之编码.py
@Editor  : 百年
@Date    :2025/3/30 21:36 
"""
name = "百年"
encoded_name = name.encode('utf-8')
print(encoded_name)
str_encode_name = str(encoded_name)
print(str_encode_name,type(str_encode_name))
strlst = str_encode_name.split("\\")
print(strlst)
# print(name.encode('utf-8'))

# print(str())
# print(ord(name))
# gbk_enc_ = name.encode('utf-8')
# print(gbk_enc_)
# print(name.encode('gbk'))
# print(name.encode('utf-8'))

# gbk_str = str(gbk_enc_)
# # print(int(gbk_enc_,16))
# print(gbk_str)
# lst = gbk_str.split("\\")
# print(lst[1:])
# for i in range(1,4):
#     print(bin(lst[i]))
# hex_num = 'e7'
# dec_num = int(hex_num,16)
# print(dec_num)
# # print(int(hex_num,16))
# print(bin(dec_num))