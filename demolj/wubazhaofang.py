import requests

response = requests.get(url='http://192.168.150.133:8050/render.html',
                        params={
                            "url": "https://bj.58.com/ershoufang/?PGTID=0d300008-0000-108f-4a34-9f3b1ee146cb&ClickID=3",
                            "wait": 3
                        })
print(response.text)
