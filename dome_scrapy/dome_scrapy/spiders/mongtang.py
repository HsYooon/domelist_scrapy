import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Mongtang_Spider(scrapy.Spider) :
    name = 'mongtang'
    start_urls = [
        'http://www.mongtang.co.kr/shop/main/index.php' # 신상품, 베스트
    ]
        
    def parse(self, response):
       uri = "http://www.mongtang.co.kr/shop"
       # 신상품 섹션
       for div in response.xpath('//td[@class="outline_side"]/table')[1].xpath('./tr/td'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./div')[0].xpath('./a/@href').get()[2:]
            img = uri + div.xpath('./div')[0].xpath('./a/img/@src').get()[2:]
            title = div.xpath('./div')[1].xpath('./div/a/text()').get()
            
            item['name'] = '블랙라이노'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '06' # 종합
            item['info'] = '11'
            yield item
        
       # 베스트 섹션
       for div in response.xpath('//td[@class="outline_side"]/table')[2].xpath('./tr/td'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./div')[0].xpath('./a/@href').get()[2:]
            img = uri + div.xpath('./div')[0].xpath('./a/img/@src').get()[2:]
            title = div.xpath('./div')[1].xpath('./div/a/text()').get()
            
            item['name'] = '블랙라이노'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '06' # 종합
            item['info'] = '12'
            yield item

        