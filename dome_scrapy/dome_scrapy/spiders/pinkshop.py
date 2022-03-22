import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class TestSpider(scrapy.Spider) :
    name = 'pinkshop'
    
    def start_requests(self):
        url = 'http://pink-shop.co.kr/'

        yield scrapy.Request(url, self.parse) # 메인 > 신상품 섹션
        
    def parse(self, response):
       uri = "http://pink-shop.co.kr"
       
       for div in response.xpath('//ul[@class="prdList column4"]/li'):
            item = DomeScrapyItem()
            
            url = uri + div.xpath('./div/p[@class="prdImg"]/a/@href').get()
            img = 'http:' + div.xpath('./div/p[@class="prdImg"]/a/img/@src').get()
            title = div.xpath('./div/p[@class="name"]/strong/a/span')[1].xpath('./text()').get()
            
            item['name'] = '핑크샵'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '11' # 의류
            item['info'] = '11'
            yield item

        