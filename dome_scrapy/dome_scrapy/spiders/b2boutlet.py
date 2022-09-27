import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class B2boutlet_Spider(scrapy.Spider):
    name = 'b2boutlet'
    info = ['11','12'] # 11: 신상품 12: 베스트 

    def start_requests(self):
        yield scrapy.Request('https://www.b2boutlet.co.kr/product/newProductList', self.parse1) # 신상품 100 
        #yield scrapy.Request('https://www.b2boutlet.co.kr/product/hitProductList', self.parse2) # 인기상품 100

    def parse1(self, response):
        uri = 'http://www.b2boutlet.co.kr'
        for div in response.css('.prdArea_1080').xpath('./ul//li'):
            item = DomeScrapyItem()

            url = uri + div.css('.prd_thumb').xpath('./div//a/@href').get()
            img = uri + div.css('.prd_thumb').xpath('./div//a//img/@src').get()
            title = div.css('.prd_disc').xpath('./div[@class="prd_name"]//a/text()').get()
            
            item['name'] = 'b2boutlet'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['info'] = self.info[0] # 신상품
            item['category'] = '01' # 종합 01
            yield item

    def parse2(self, response):
        uri = 'http://www.b2boutlet.co.kr'
        for div in response.css('.prdArea_1080').xpath('./ul//li'):
            item = DomeScrapyItem()

            url = uri + div.css('.prd_thumb').xpath('./div//a/@href').get()
            img = uri + div.css('.prd_thumb').xpath('./div//a//img/@src').get()
            title = div.css('.prd_disc').xpath('./div[@class="prd_name"]//a/text()').get()
            
            item['name'] = 'b2boutlet'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['info'] = self.info[1] # 베스트
            item['category'] = '01' # 종합 01
            yield item
            