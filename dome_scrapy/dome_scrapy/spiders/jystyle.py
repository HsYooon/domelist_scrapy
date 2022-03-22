import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Jystyle_Spider(scrapy.Spider) :
    name = 'jystyle'
    
    def start_requests(self):
        urls = [
        'https://www.jystyle.net/',
        ]
        yield scrapy.Request(urls[0], self.parse) # 메인 > 신상품 섹션
        
    def parse(self, response):
       uri = "https://www.jystyle.net"

       for div in response.xpath('//ul[@class="prdList grid4"]/li'):
            item = DomeScrapyItem()
            url = uri # + div.xpath('./div[@class="thumbnail outline"]/a/@href').get()
            img = 'http:' + div.xpath('./div[@class="thumbnail outline"]/a/div[@class="normal_thumb"]/img/@src').get()
            title = div.xpath('./div[@class="description"]/p[@class="name"]/a/text()').get().strip(' ')

            item['name'] = '제이와이스타일'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '11' # 종합
            item['info'] = '11' # 신상품
            yield item
       

        