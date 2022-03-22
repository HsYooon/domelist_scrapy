import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Dogsclub_Spider(scrapy.Spider) :
    name = 'dogsclub'
    start_urls = [
        'http://www.dogsclub.co.kr' # 메인 > 신상품 섹션
    ]

    def parse(self, response):

        uri = 'http://www.dogsclub.co.kr'

        # 신상품 섹션
        for div in response.xpath('//div[@class="item-list"]')[1].xpath('./table/tbody//td'):
            item = DomeScrapyItem()

            url = uri # + div.xpath('./ul/li')[0].xpath('./div//a/@href').get()
            img = uri + div.xpath('./ul/li')[0].xpath('./div//a//img/@src').get()
            title = div.xpath('./ul/li')[1].xpath('./text()').get()

            item['name'] = '독스클럽'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '08' # 애완
            item['info'] = '11' # 신상품
            yield item

        # 베스트상품 섹션
        for div in response.xpath('//div[@class="item-list"]')[0].xpath('./table/tbody//td'):
            item = DomeScrapyItem()

            url = uri # + div.xpath('./ul/li')[0].xpath('./div//a/@href').get()
            img = uri + div.xpath('./ul/li')[0].xpath('./div//a//img/@src').get()
            title = div.xpath('./ul/li')[1].xpath('./text()').get()

            item['name'] = '독스클럽'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '08' # 애완
            item['info'] = '12' # 베스트
            yield item

        