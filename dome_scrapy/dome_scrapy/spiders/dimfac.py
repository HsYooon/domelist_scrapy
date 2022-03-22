import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Dimfac_Spider(scrapy.Spider) :
    name = 'dimfac'
    
    def start_requests(self):
        urls = [
        'https://www.dimfac.co.kr/product/list.html?cate_no=29', # TOP
        'https://www.dimfac.co.kr/product/list.html?cate_no=59', # Man Pants
        'https://www.dimfac.co.kr/product/list.html?cate_no=30', # Woman Pants
        ]
        for url in urls :
            yield scrapy.Request(url, self.parse) 
        
    def parse(self, response):
       uri = "https://www.dimfac.co.kr"

       for div in response.xpath('//ul[@class="prdList column4"]/li'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./div/a/@href').get()
            img = 'http:' + div.xpath('./div/a/img/@src').get()
            title = div.xpath('./div/p[@class="name"]/a/span/text()').get()
            
            item['name'] = '딤팩'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '11' # 의류
            item['info'] = '12'
            yield item
       

        