import scrapy

class Dmoz(scrapy.Spider):
    name = "dmoz"
    # allowed_domain=["weibo.cn"]
    start_urls = ["http://www.liaoxuefeng.com"]

    def parse(self, response):
        print("开始执行parse方法")
        filename = response.body
        print(filename)

        with open('filename', 'w',encoding='utf-8') as f:
            f.write(str(response.body))