"""
@File    :wangyinews.py
@Editor  : 百年
@Date    :2025/3/15 21:50 
"""
import requests
from lxml import etree

response = requests.get(
    url='http://192.168.150.133:8050/render.html',
    params={
        "url":"",
        "wait":5
    }
)

'''
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

  return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har(),
  }
end'''

# timestamp:2’25‘’29‘’‘