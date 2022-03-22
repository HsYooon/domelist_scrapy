import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Byramee_Spider(scrapy.Spider) :

    name = 'byramee'
    info = ['11','12'] # 11 : 신상품 12: 베스트상품
    uri = 'http://www.byramee.com'
    start_urls = [
        'http://www.byramee.com' # 메인 > 신상품 섹션
    ]

    def parse(self, response):
        # 신상품 섹션
        for div in response.xpath('//div[@class="item-list"]')[1].xpath('./table/tbody//td'):
            item = DomeScrapyItem()

            url = self.uri # + div.xpath('./ul/div/div[@class="prd-thumb"]//a/@href').get()
            img = self.uri + div.xpath('./ul/div/div[@class="prd-thumb"]//a//img/@src').get()
            title = div.xpath('./ul/div/li/text()').get()

            item['name'] = '바이라미'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '11' # 의류
            item['info'] = self.info[0] # 신상품
            yield item

        # 베스트 상품
        for div in response.xpath('//div[@class="item-list"]')[2].xpath('./table/tbody//td'):
            item = DomeScrapyItem()

            url = self.uri # + div.xpath('./ul/div/div[@class="prd-thumb"]//a/@href').get()
            img = self.uri + div.xpath('./ul/div/div[@class="prd-thumb"]//a//img/@src').get()
            title = div.xpath('./ul/div/li/text()').get()

            item['name'] = '바이라미'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '11' # 의류
            item['info'] = self.info[1] # 베스트
            yield item