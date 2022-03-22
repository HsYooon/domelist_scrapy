import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Innovill_Spider(scrapy.Spider) :
    name = 'innovill'
    
    def start_requests(self):
        urls = [
        'http://www.innovill.com/shop/shopbrand.html?xcode=030&type=P', # 신상품
        'http://www.innovill.com/shop/shopbrand.html?xcode=043&type=P'  # 베스트 
        ]
        yield scrapy.Request(urls[0], self.parse_new) # 메인 > 신상품 섹션 
        yield scrapy.Request(urls[1], self.parse_best) # 인기상품 100
        
    def parse_new(self, response):
       uri = "http://www.innovill.com"
       for div in response.xpath('//div[@class="prd_tbl_area"]'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./a/@href').get()
            img = uri + div.xpath('./a/img/@src').get()
            title = div.xpath('./div[@class="prd_info_box"]/p[@class="prd_name"]/text()').get()
            
            item['name'] = '이노빌'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '11' # 의류
            item['info'] = '11'
            yield item
    
    def parse_best(self, response):
       uri = "http://www.innovill.com"
       for div in response.xpath('//div[@class="prd_tbl_area"]'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./a/@href').get()
            img = uri + div.xpath('./a/img/@src').get()
            title = div.xpath('./div[@class="prd_info_box"]/p[@class="prd_name"]/text()').get()
            
            item['name'] = '이노빌'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '11' # 의류
            item['info'] = '12'
            yield item

        