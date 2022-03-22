import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class B2bpet_Spider(scrapy.Spider) :
    name = 'b2bpet'
    
    def start_requests(self):
        url = 'http://b2bpet.co.kr'
        yield scrapy.Request(url, self.parse)


    def parse(self, response):
       uri = "http://b2bpet.co.kr"
       
       # 신상품
       for div in response.xpath('//ul[@class="prdList grid4"]')[0].xpath('./li'):
            item = DomeScrapyItem()
            
            url = uri + div.xpath('./div[1]/a/@href').get()
            img = 'http:' + div.xpath('./div[1]/a/img/@src').get()
            title = div.xpath('./div[2]/span/a/span[2]/text()').get()
            
            item['name'] = '비투비펫'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '08' # 애견
            item['info'] = '11'
            yield item

       # 베스트
       for div in response.xpath('//ul[@class="prdList grid4"]')[1].xpath('./li'):
            item = DomeScrapyItem()
            
            url = uri + div.xpath('./div[1]/a/@href').get()
            img = 'http:' + div.xpath('./div[1]/a/img/@src').get()
            title = div.xpath('./div[2]/span/a/span[2]/text()').get()
            
            item['name'] = '비투비펫'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '08' # 애견
            item['info'] = '12'
            yield item