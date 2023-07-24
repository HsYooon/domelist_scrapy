import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Nonda_Spider(scrapy.Spider) :
    name = 'nonda'
    start_urls = [
        'http://nonda.co.kr/' # 메인
    ]
        
    def parse(self, response):
       uri = 'http://nonda.co.kr'

       for div in response.xpath('//*[@id="container"]/div[3]/div[1]/ul/li'):
            item = DomeScrapyItem()
            url = uri
            img = 'http:' + div.xpath('./div/div[1]/a/img/@src').get()
            title = div.xpath('./div/div[2]/p/a/span[2]/text()').get()

            item['name'] = '논다'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '08' # 반려/애완
            item['info'] = '11' # 신상품
            yield item

       for div in response.xpath('//*[@id="container"]/div[3]/div[2]/ul/li'):
            item = DomeScrapyItem()
            url = uri
            img = 'http:' + div.xpath('./div/div[1]/a/img/@src').get()
            title = div.xpath('./div/div[2]/p/a/span[2]/text()').get()

            item['name'] = '논다'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '08' # 반려/애완
            item['info'] = '12' # 베스트
            yield item

        