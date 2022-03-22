import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Dodomall_Sprider(scrapy.Spider) :

    name = 'dodomall'
    info = ['11','12'] # 11 : 신상품 12: 베스트상품
    uri = 'https://www.dodomall.co.kr'
    start_urls = [
        'http://www.dodomall.co.kr' # 메인 > 신상품 섹션, 베스트 상품 섹션
    ]

    def parse(self, response):
        # 신상품 섹션
        for div in response.xpath('//div[@class="product_slider2"]')[0].xpath('./ul[@class="prdList"]').xpath('./li'):
            item = DomeScrapyItem()

            url = self.uri + div.xpath('./div//a/@href').get()
            img = self.uri + div.xpath('./div//a//img/@src').get()
            title = div.xpath('./div/div//p[@class="name"]//a/text()').get()

            item['name'] = '도도몰'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '06' # 자동차
            item['info'] = '11' # 신상품
            yield item

        for div in response.xpath('//div[@class="special_product_area"]//div[@class="widget_normal_product"]')[0].xpath('./ul/li'):
            item = DomeScrapyItem()

            url = self.uri + div.xpath('./div//a/@href').get()
            img = self.uri + div.xpath('./div//a//img/@src').get()
            title = div.xpath('./div/div//p[@class="name"]//a/text()').get()

            item['name'] = '도도몰'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '06' # 자동차
            item['info'] = '12' # 베스트
            yield item