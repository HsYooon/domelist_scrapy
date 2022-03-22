import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Plusb2bSpider(scrapy.Spider) : 
    name = 'plusb2b'
    start_urls = [
       'https://plusb2b.com/' # 메인페이지 > 신상품 섹션 (메인페이지 외에 접근 불가)
    ]

    def parse(self, response):

        for div in response.xpath('//ul[@class="prdList grid6"]')[0].xpath('./li'):
            item = DomeScrapyItem()

            uri = 'https://plusb2b.com'
            # url_tag = div.xpath('./div[@class="thumbnail outline"]//a/@href').get()
            url = uri # + url_tag

            img = div.xpath('./div[@class="thumbnail outline"]//a//div[@class="normal_thumb"]//img/@src').get()
            title = div.xpath('./div[@class="description"]//p//a/text()').get()
            
            item['name'] = 'plusb2b'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['info'] = '11'
            item['category'] = '05' # 헬스케어
            yield item