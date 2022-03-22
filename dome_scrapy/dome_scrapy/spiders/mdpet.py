import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Mdpet_Spider(scrapy.Spider) :
    name = 'mdpet'
    
    def start_requests(self):
        url = 'http://www.mdpet.co.kr/'
        yield scrapy.Request(url, self.parse)


    def parse(self, response):
       uri = "http://www.mdpet.co.kr"
       
       # 신상품
       for div in response.xpath('//ul[@class="prdList column6"]')[0].xpath('./li'):
            item = DomeScrapyItem()
            
            url = uri #+ div.xpath('./div/a/@href').get()
            img = 'http:' + div.xpath('./div/a/img/@src').get()
            title = div.xpath('./div/p/a/span[2]/text()').get()
            
            item['name'] = '엠디펫'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '08' # 애견
            item['info'] = '11'
            yield item
       
       # 베스트
       for div in response.xpath('//ul[@class="prdList column6"]')[1].xpath('./li'):
            item = DomeScrapyItem()
            
            url = uri #+ div.xpath('./div/a/@href').get()
            img = 'http:' + div.xpath('./div/a/img/@src').get()
            title = div.xpath('./div/p/a/span[2]/text()').get()
            
            item['name'] = '엠디펫'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '08' # 애견
            item['info'] = '12'
            yield item
       