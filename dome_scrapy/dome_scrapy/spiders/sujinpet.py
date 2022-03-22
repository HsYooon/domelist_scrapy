import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Sujinpet_Spider(scrapy.Spider) :

    name = 'sujinpet'
    start_urls = [
        'http://www.sujinpet.co.kr' # 메인 > 신상품 섹션
    ]

    def parse(self, response):

        uri = 'http://www.sujinpet.co.kr'

        # 신상품 섹션
        for div in response.xpath('//div[@class="cboth prd-list list02"]')[1].xpath('./table/tbody//td'):
            item = DomeScrapyItem()

            url = uri # + div.xpath('./div/div[@class="thumb"]//a/@href').get()
            img = uri + div.xpath('./div/div[@class="thumb"]//a//img/@src').get()
            title = div.xpath('./div/ul[@class="info"]/li[@class="dsc"]/a/text()').get().strip()

            item['name'] = '수진펫'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '08' # 애완
            item['info'] = '11' # 신상품
            yield item
        
        # 베스트상품 섹션
        for div in response.xpath('//div[@class="cboth prd-list list02"]')[0].xpath('./table/tbody//td'):
            item = DomeScrapyItem()

            url = uri # + div.xpath('./div/div[@class="thumb"]//a/@href').get()
            img = uri + div.xpath('./div/div[@class="thumb"]//a//img/@src').get()
            title = div.xpath('./div/ul[@class="info"]/li[@class="dsc"]/a/text()').get().strip()

            item['name'] = '수진펫'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '08' # 애완
            item['info'] = '12' # 신상품
            yield item

        