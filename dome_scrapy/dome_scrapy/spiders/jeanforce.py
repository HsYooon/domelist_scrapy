import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Jeanforce_Spider(scrapy.Spider) :
    name = 'jeanforce'
    start_urls = [
        'http://rooala1.cafe24.com/' # 베스트 
    ]
        
    def parse(self, response):
       uri = "http://rooala1.cafe24.com"
       for div in response.xpath('//ul[@class="prdList column5"]/li'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./div/a/@href').get()
            img = "http:" + div.xpath('./div/a/img/@src').get()
            title = div.xpath('./div/p[@class="name"]/a/span/text()').get()
            
            item['name'] = '진포스'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '11' # 종합
            item['info'] = '12'
            yield item
       

        