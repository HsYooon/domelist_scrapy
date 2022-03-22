import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Wehayou_Spider(scrapy.Spider) :
    name = 'wehayou'
    
    def start_requests(self):
        url = 'http://www.wehayou.com/'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
       # 신상품
       for div in response.xpath('//ul[@class="image_box"]')[0].xpath('./li'):
            item = DomeScrapyItem()
            url = div.xpath('./a/@href').get()
            img = div.xpath('./a/span[1]/img/@src').get()
            title = div.xpath('./a/span[2]/strong/text()').get()
            
            item['name'] = '위하여'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '02' # 생활
            item['info'] = '11'
            yield item
        # 베스트
       for div in response.xpath('//ul[@class="image_box"]')[1].xpath('./li'):
            item = DomeScrapyItem()
            url = div.xpath('./a/@href').get()
            img = div.xpath('./a/span[1]/img/@src').get()
            title = div.xpath('./a/span[2]/strong/text()').get()
            
            item['name'] = '위하여'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '02' # 생활
            item['info'] = '12'
            yield item
       