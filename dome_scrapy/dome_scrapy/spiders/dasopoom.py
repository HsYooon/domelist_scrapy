import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Soggupnoli_Spider(scrapy.Spider) :
    name = 'dasopoom'
    start_urls = [
        'http://www.dasopoom.com' # 메인 > 신상품 섹션
    ]

    def parse(self, response):

        uri = 'http://www.dasopoom.com'

        # 신상품 섹션
        for div in response.xpath('//ul[@class="prdList column5"]/li'):
            item = DomeScrapyItem()

            url = uri + div.xpath('./div/a/@href').get()
            img = uri + div.xpath('./div/a/img/@src').get()[2:]
            title = div.xpath('./div/p[@class="name"]/a/span/text()').get()

            item['name'] = '다소품'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '03' # 인테리어/소품
            item['info'] = '11' # 신상품
            yield item

    
        