"""
@File    :wangyinews.py
@Editor  : 百年
@Date    :2025/3/15 21:50 
"""
import json

import requests
from lxml import etree

lua_source = """
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  
  get_btn_display = splash:jsfunc([[
    function(){
    return document.getElementsByClassName('load_more_btn')[0].style.display;
  }
    ]])
  while(true)
  do
  splash:runjs("document.getElementsByClassName('load_more_btn')[0].scrollIntoView(true)")
  splash:select(".load_more_btn").click()
  splash:wait(1)
  -- 判断load_more_btn是否为none
  display = get_btn_display()
  if(display == 'none')
  then 
      break
  end
 end
 assert(splash:wait(2))
return {
    html = splash:html(),
}
end

"""
response = requests.get(
    url='http://192.168.150.133:8050/execute',
    params={
        "url": "https://news.163.com/domestic/",
        "wait": 5,
        "lua_source": lua_source,
    }
)
response.encoding = response.apparent_encoding

print(response.text)
content_json = response.json()  #将json字符串转为python字典
print(content_json['html'][:2000]) #获取html源码
tree = etree.HTML(content_json['html'])
# titles = tree.xpath('//div[@class="na_detail clearfix"]//h3/a/text()')
titles = tree.xpath('//div[contains(@class, "news_title")]//a/text()')
if titles:
    print("\nFound titles:")
    for title in titles:
        print(title.strip())
else:
    print("No titles found.")
# print(title)


