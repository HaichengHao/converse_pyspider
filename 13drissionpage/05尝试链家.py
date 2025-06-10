"""
@File    :05尝试链家.py
@Editor  : 百年
@Date    :2025/5/30 22:47 
"""
from DrissionPage import WebPage,ChromiumPage,SessionPage
page = WebPage()
page.get('https://sy.lianjia.com/?utm_source=biying&utm_medium=pinzhuan&utm_term=biaoti&utm_content=biaotimiaoshu&utm_campaign=wybeijing')
loginbtn = page.ele('.reg')
loginbtn.click()

phone_num_input = page.ele('.phonenum_input')
phone_num_input.input('18864771568')

vfbycaid = page.ele('.addtional_a send_login_message_verify _color')
vfbycaid.click()

vf_input = page.ele('.code_type messageverifycode_input')
vf = input('输入手机的验证码>>')
vf_input.input(vf)

lg_btn = page.ele('.btn confirm_btn login_panel_op login_submit _bgcolor')
lg_btn.click()



