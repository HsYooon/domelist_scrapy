import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Zseller_Spider(scrapy.Spider) :
    name = 'zseller'
    start_urls = [
       'https://www.zseller.kr/index.html' #메인 > 신상품 섹션 (10개)
    ]

    def parse(self, response):
        for div in response.xpath('//div[@id="wrap-container"]/div[2]//dl[@class="item-list"]'):
            item = DomeScrapyItem()
            uri = 'https://www.zseller.kr'
            url_tag = div.css('.thumb').xpath('.//a/@href').get()
            url = uri + url_tag
            img_tag = div.css('.thumb').xpath('.//a//img/@src').get()
            img = uri + img_tag
            title = div.xpath('.//dd/ul/li[1]/text()').get()
            
            item['name'] = '제트셀러'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['info'] = '11'
            item['category'] = '02'
            yield item