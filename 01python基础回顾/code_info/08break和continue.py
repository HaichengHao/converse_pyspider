# editor: 百年
# time: 2024/3/1 14:52
'''while True:
    content=input('请输入要说的内容(q结束)：')
    if content=='q': # 双等号用于判断
        break
    print("发送给下路射手:",content)'''

# 从一数到十 不要四
i=1
while i <11:
    if i == 4:
        i+=1
        continue  #终止当前循环进入下一次循环
    print(i)
    i+=1
