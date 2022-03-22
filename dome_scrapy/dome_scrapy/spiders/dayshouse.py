import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Dayshouse_Spider(scrapy.Spider) :
    name = 'dayshouse'
    start_urls = [
        'http://dayshouse.co.kr/index.html' # 신상품 섹션
    ]
        
    def parse(self, response):
       item = DomeScrapyItem()
       home = "http://dayshouse.co.kr/index.html"
       
       for div in response.xpath('//ul[@class="prdList column4"]/li'):
           url = home
           img = 'https:' + div.xpath('./div/a/img/@src').get()
           title = div.xpath('./div/p/a/span/text()').get()

           item['name'] = '데이스하우스'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '03' # 인테리어/소품
           item['info'] = '11' # 신상품
           yield item

        