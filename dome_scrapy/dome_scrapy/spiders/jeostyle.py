import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Jeostyle_Spider(scrapy.Spider) :
    name = 'jeostyle'
    start_urls = [
        'https://jeo-style.com/index.html' # 메인 > 신상품 섹션
    ]

    def parse(self, response):

        uri = 'https://jeo-style.com'

        # 신상품 섹션
        for div in response.xpath('//ul[@class="prdList column4"]')[1].xpath('./li'):
            item = DomeScrapyItem()
            
            url = uri + div.xpath('./div//a/@href').get()
            img = div.xpath('./div//a//img/@src').get()
            if img.find('http') == -1 :
                img = 'https:' + img
            title = div.xpath('./div/p[@class="name"]/a/span/text()').get()
           
            item['name'] = '제오스타일'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '11' # 의류
            item['info'] = '11' # 신상품
            yield item

        # 베스트 섹션
        for div in response.xpath('//ul[@class="prdList column4"]')[0].xpath('./li'):
            item = DomeScrapyItem()
            
            url = uri + div.xpath('./div//a/@href').get()
            img = div.xpath('./div//a//img/@src').get()
            if img.find('http') == -1 :
                img = 'https:' + img
            title = div.xpath('./div/p[@class="name"]/a/span/text()').get()
            
            item['name'] = '제오스타일'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '11' # 애완
            item['info'] = '12' # 베스트
            yield item