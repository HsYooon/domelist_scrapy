import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Plala_Spider(scrapy.Spider) :
    name = 'plala'
    start_urls = [
       'https://plala.co.kr/' # 메인페이지 > 신상품 섹션 (메인페이지 외 접근 불가)
    ]

    def parse(self, response):

        for div in response.xpath('//ul[@class="prdList column5"]')[0].xpath('./li'):
            item = DomeScrapyItem()
            uri = 'https://plala.co.kr'

            box = div.xpath('./div[@class="box"]')
            # url_tag = box.xpath('./a/@href').get()
            url = uri # + url_tag

            img_tag = box.xpath('./a//img/@src').get()
            img = 'https:' + img_tag

            title = box.xpath('./p[@class="name"]//strong//a//span[2]/text()').get()
            
            
            item['name'] = '플라라'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['info'] ='11'
            item['category'] = '02' # 주방 인테리어
            yield item