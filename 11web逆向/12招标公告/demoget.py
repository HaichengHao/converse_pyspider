import requests
# url = 'https://ctbpsp.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/2?province=&industry=&type__1017=n4%2BhDKAKD5YvPQqGKG%3DD%2FtF4BKOefDYqxW7wID'
url = 'https://ctbpsp.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/1?province=&industry=&type__1017=n4%2BxnDBDgDcDy0DRDxlxGhbCoG%3Dkwb7eKhD'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}

response = requests.get(url=url,headers=headers)
# response.encoding = response.apparent_encoding
print(response.text)