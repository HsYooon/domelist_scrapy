import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Gogob2b_Spider(scrapy.Spider) :
    name = 'gogob2b'
    start_urls = [
        'http://gogob2b.co.kr/' # 메인
    ]
        
    def parse(self, response):
       uri = 'http://gogob2b.co.kr'

       for div in response.xpath('//*[@id="tabContent1"]/div/div/ul/li'):
            item = DomeScrapyItem()

            url = uri
            img = 'http:' + div.xpath('./div/div[1]/a/img/@src').get()
            title = div.xpath('./div/div[2]/div/a/span[2]/text()').get()
            
            item['name'] = '고고비투비'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '11' # 신상품
            yield item

       for div in response.xpath('//*[@id="contents"]/section[4]/div[2]/div/ul/li'):
            item = DomeScrapyItem()

            url = uri
            img = 'http:' + div.xpath('./div/div[1]/a/img/@src').get()
            title = div.xpath('./div/div[2]/div/a/span[2]/text()').get()
           
            item['name'] = '고고비투비'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '12' # 베스트
            yield item

        