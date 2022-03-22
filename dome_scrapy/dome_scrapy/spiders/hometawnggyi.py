import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Hometawnggyi_Spider(scrapy.Spider) :
    name = 'hometawnggyi'
    
    def start_requests(self):
        url = 'http://shop1.microsoft990.cafe24.com/'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
       uri = "http://shop1.microsoft990.cafe24.com"
       
       # 베스트
       for div in response.xpath('//ul[@class="prdList grid3"]').xpath('./li'):
            item = DomeScrapyItem()
            url = uri # + div.xpath('./div[1]/a/@href').get()
            img = 'http:' + div.xpath('./div[1]/a/img/@src').get()
            title = div.xpath('./div[2]/strong/a/span[2]/text()').get()
            
            item['name'] = '홈타운지'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '02' # 종합
            item['info'] = '12'
            yield item
       