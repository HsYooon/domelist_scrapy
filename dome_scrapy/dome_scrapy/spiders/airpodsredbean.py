import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Airpodsredbean_Spider(scrapy.Spider) :
    name = 'airpodsredbean'
    
    def start_requests(self):
        url = 'https://airpodsredbean.shop/index.html'
        yield scrapy.Request(url, self.parse)


    def parse(self, response):
       uri = "https://airpodsredbean.shop"
       
       # 베스트
       for div in response.xpath('//ul[@class="prdList column4"]').xpath('./li'):
            item = DomeScrapyItem()
            
            url = uri + div.xpath('./div/a/@href').get()
            img = 'http:' + div.xpath('./div/a/img/@src').get()
            title = div.xpath('./div/p/strong/a/span[2]/text()').get()
            
            item['name'] = '에어팥빙수'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '09' # 디지털/가전
            item['info'] = '12'
            yield item
       