import scrapy
from urllib.parse import urljoin


class SjSpider(scrapy.Spider):
    name = "sj"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://m.23shu.net/user/mark/index.html"]

    #     #tips: 方案1
    #     cookie_str = """
    #     __51vcke__Je024mWmwNSOFcwg=b1f6f044-41d6-56b5-a13d-9c1424a401d6; __51vuft__Je024mWmwNSOFcwg=1741227413069; PTCMS_userid=36476; PTCMS_username=shun; PTCMS_token=37ff97eefe21333ab4e4f3ce1a2c122c; __51uvsct__Je024mWmwNSOFcwg=3; PTCMS_marknum=1; __vtins__Je024mWmwNSOFcwg=%7B%22sid%22%3A%20%2258ab6685-c94b-545c-9c6c-e6261040a2c7%22%2C%20%22vd%22%3A%202%2C%20%22stt%22%3A%2099589%2C%20%22dr%22%3A%2099589%2C%20%22expires%22%3A%201741232070060%2C%20%22ct%22%3A%201741230270060%7D
    # """
    #     cookies = {} #step 1: 创建一个字典用于保存cookie这种的键值对，因为start_requests()这个方法中传入的cookies参数需要是一个字典类型
    #     for cookie in cookie_str.split('; '): #tips:切分后的串形成了一个列表，并对列表中的每个元素进行遍历
    #         key, value = cookie.split('=') #tips:再将每个元素按照等号分割开来，分开的连个元素一个作为键，一个作为值
    #         cookies[key.strip()] = value.strip() #tips:再将键值对匹配，这样cookies字典就填充完毕
    #     # step 2:重写start_requests方法,让其携带登录后的书架信息的cookie然后就可以直接进行爬取
    #     def start_requests(self):
    #         yield scrapy.Request(
    #             url=self.start_urls[0],
    #             cookies = self.cookies,

    # )

    # 方案2 进行模拟登录
    url = 'https://m.23shu.net/user/public/login.html'
    user_name = input('请输入用户名:')
    passwd = input('请输入密码:')

    def start_requests(self):
        data = {
            'comeurl': '/user/mark/index.html',
            'username': self.user_name,
            'password': self.passwd
        }
        # 还有一种不用FormRequest，直接用Request带数据
        # yield scrapy.Request(
        #     url=self.url,
        #     method='post',
        #     body=f'comeurl=%2Fuser%2Fmark%2Findex.html&username={self.user_name}&password={self.passwd}',  # 这种很low
        #     callback=self.parse
        # )
        yield scrapy.FormRequest(url=self.url,callback=self.parse,formdata=data)

    def parse(self, response):
        # print(response.text)
        # tips:方案2需要再次请求那个书架的url,因为刚才上面的请求是对登录用的url发的
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse_detail)
        # important:这样做就跟之前学的session处理一样,这样我们处理完了就跟已经登录了一样，是携带了书架的信息的

    def parse_detail(self, response):
        # print(response.text)
        a_s = response.xpath('//div[@class="pt-name"]/a')
        for a in a_s:
            title = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            url = urljoin(response.url,href)  # 利用urljoin对不完整的href进行拼接

            print(f'Title: {title}, URL: {url}')


