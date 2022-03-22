import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Domegod_Sprider(scrapy.Spider) :

    name = 'domegod'
    start_urls = [
        'http://domegod.com' # 메인 > 신상품 섹션
    ]

    def parse(self, response):

        uri = 'http://domegod.com'

        # 신상품 섹션
        for div in response.xpath('//ul[@class="prdList"]').xpath('./li'):
            item = DomeScrapyItem()

            url = uri + div.xpath('./div[@class="imgArea"]//a/@href').get()
            img = 'http:' + div.xpath('./div[@class="imgArea"]//a//img/@src').get()
            title = div.xpath('./div[@class="infoArea"]/div/div//ul[@class="cf"]//li[@class="name"]//a/span')[1].xpath('text()').get()

            item['name'] = '도매갓'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '11' # 의류
            item['info'] = '11' # 신상품
            yield item