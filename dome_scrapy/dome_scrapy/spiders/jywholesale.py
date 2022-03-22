import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Jywholesale_Spider(scrapy.Spider) :
    name = 'jywholesale'
    
    def start_requests(self):
        urls = ['https://jywholesale.co.kr/home','https://jywholesale.co.kr/BEST']
        yield scrapy.Request(urls[0], self.parse_new)
        yield scrapy.Request(urls[1], self.parse_best)

    def parse_new(self, response):
       uri = "https://jywholesale.co.kr"
       
       for div in response.xpath('//div[@class="shop-item _shop_item"]'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./div[1]/a/@href').get()
            img = div.xpath('./div[1]/a/img/@data-original').get()
            title = div.xpath('./div[2]/a/div/h2/text()').get()
            
            item['name'] = '정윤유통'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '04' # 식품
            item['info'] = '11' # 신상품
            yield item
    
    def parse_best(self, response):
       uri = "https://jywholesale.co.kr"
       
       for div in response.xpath('//div[@class="shop-item _shop_item"]'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./div[1]/a/@href').get()
            img = div.xpath('./div[1]/a/img/@data-original').get()
            title = div.xpath('./div[2]/a/div/h2/text()').get()
            
            item['name'] = '정윤유통'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '04' # 식품
            item['info'] = '12' # 베스트
            yield item