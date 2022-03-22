import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Pettory_Spider(scrapy.Spider) :
    name = 'pettory'
    
    def start_requests(self):
        url = 'http://www.pettory.com/'
        yield scrapy.Request(url, self.parse)


    def parse(self, response):
       uri = "http://www.pettory.com"
       
       # 베스트
       for div in response.xpath('//ul[@class="prdList grid7"]')[0].xpath('./li'):
            item = DomeScrapyItem()
            
            url = uri # + div.xpath('./div[1]/a/@href').get()
            img = 'http:' + div.xpath('./div[1]/a/img/@src').get()
            title = div.xpath('./div[2]/strong/a/span[2]/text()').get()
            
            item['name'] = '펫토리'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '08' # 애견
            item['info'] = '12'
            yield item

       # 신상품
       for div in response.xpath('//ul[@class="prdList grid7"]')[1].xpath('./li'):
            item = DomeScrapyItem()
            
            url = uri # + div.xpath('./div[1]/a/@href').get()
            img = 'http:' + div.xpath('./div[1]/a/img/@src').get()
            title = div.xpath('./div[2]/strong/a/span[2]/text()').get()
            
            item['name'] = '펫토리'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '08' # 애견
            item['info'] = '11'
            yield item
       