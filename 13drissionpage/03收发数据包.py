# @Author    : 百年
# @FileName  :03收发数据包.py
# @DateTime  :2025/5/30 19:33
from DrissionPage import ChromiumPage,SessionPage

#创建页面请求对象
page = SessionPage()

#爬取前三页
for i in range(1,4):
    #访问第i页
    page.get(f'https://gitee.com/explore/all?page={i}')
    #提取每一页的库链接,即a标签中的链接
    #这里用的是类选择器
    links=page.eles('.title project-namespace-path') #important:注意这里是eles,和selenium中find_element和find_elements很像
    #遍历获得所有的link
    for link in links:
        # print(link)
        ''' 获得的是这样的对象,很像之前的连接提取器
        <SessionElement a title='dromara/Sa-Token' target='_blank' class='title project-namespace-path' href='https://gitee.com/dromara/sa-token'>
<SessionElement a title='若依/RuoYi' target='_blank' class='title project-namespace-path' href='https://gitee.com/y_project/RuoYi'>
        '''
        print(link.text,link.link) #这里提取的方式和链接提取器简直一模一样
'''
dromara/Sa-Token https://gitee.com/dromara/sa-token
若依/RuoYi https://gitee.com/y_project/RuoYi
lengleng/pig https://gitee.com/log4j/pig
小诺/Snowy https://gitee.com/xiaonuobase/snowy
MAKU/maku-boot https://gitee.com/makunet/maku-boot
铭飞/MCMS https://gitee.com/mingSoft/MCMS
微同软件/微同商城 https://gitee.com/fuyang_lipengjun/platform
macro/mall https://gitee.com/macrozheng/mall
卓源软件/JeeSite V5.x https://gitee.com/thinkgem/jeesite5
Lang/大屏数据展示模板 https://gitee.com/lvyeyou/DaShuJuZhiDaPingZhanShi
chinabugotech/hutool https://gitee.com/chinabugotech/hutool
张恕征/zheng https://gitee.com/shuzheng/zheng
纵之格/ShopXO https://gitee.com/zongzhige/shopxo
keking/kkFileView https://gitee.com/kekingcn/file-online-preview
smallchill/SpringBlade https://gitee.com/smallc/SpringBlade
若依/RuoYi-Cloud https://gitee.com/y_project/RuoYi-Cloud
江离/Cloud-Platform https://gitee.com/geek_qi/cloud-platform
程序猿DD/SpringBoot-Learning https://gitee.com/didispace/SpringBoot-Learning
Binary Wang/WxJava https://gitee.com/binary/weixin-java-tools
LongbowEnterprise/BootstrapAdmin https://gitee.com/LongbowEnterprise/BootstrapAdmin
JEECG/JeecgBoot https://gitee.com/jeecg/JeecgBoot
Layui/layui https://gitee.com/layui/layui
众邦科技/CRMEB开源商城系统 https://gitee.com/ZhongBangKeJi/CRMEB
stylefeng/Guns https://gitee.com/stylefeng/guns
LongbowEnterprise/BootstrapBlazor https://gitee.com/LongbowEnterprise/BootstrapBlazor
zuohuaijun/Admin.NET https://gitee.com/zuohuaijun/Admin.NET
dromara/go-view https://gitee.com/dromara/go-view
dotNET China/Furion https://gitee.com/dotnetchina/Furion
爬山虎/ndd https://gitee.com/cxasm/notepad--
小柒2012商城/spring-boot-seckill https://gitee.com/52itstyle/spring-boot-seckill
MAKU/maku-generator https://gitee.com/makunet/maku-generator
许雪里/xxl-job https://gitee.com/xuxueli0323/xxl-job
季圣华/管伊佳ERP https://gitee.com/jishenghua/JSH_ERP
轨迹/J-IM https://gitee.com/xchao/j-im
计全科技/jeepay https://gitee.com/jeequan/jeepay
赤龙ERP/赤龙ERP https://gitee.com/redragon/redragon-erp
anji-plus/AJ-Report https://gitee.com/anji-plus/report
人人开源/renren-security https://gitee.com/renrenio/renren-security
dromara/Jpom https://gitee.com/dromara/Jpom
baomidou/mybatis-plus https://gitee.com/baomidou/mybatis-plus
@HuangBingGui/JeeSpringCloud https://gitee.com/JeeHuangBingGui/jeeSpringCloud
小柒2012商城/小七商城小程序-商城支付 https://gitee.com/52itstyle/spring-boot-pay
dromara/MaxKey https://gitee.com/dromara/MaxKey
卓源软件/JeeSite Spring Cloud https://gitee.com/thinkgem/jeesite-cloud
Javen/IJPay https://gitee.com/javen205/IJPay

Process finished with exit code 0
'''
# important:.text获取元素的文本，.link获取元素的href或src属性