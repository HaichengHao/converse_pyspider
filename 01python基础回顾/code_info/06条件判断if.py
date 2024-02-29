# editor: 百年
# time: 2024/2/29 11:24
#
yourMoney=int(input('请输入您的账户余额'))
if 70000<yourMoney<100000:
    print('你的钱结婚没戏，不过你可以买辆车出去透透气')
elif 130000<yourMoney<=150000:
    print('你的钱能买辆好车')
elif yourMoney>=200000:
    print('结婚吧，结婚后你的钱就剩{0}'.format(yourMoney-200000))
else:
    print('再攒攒吧')