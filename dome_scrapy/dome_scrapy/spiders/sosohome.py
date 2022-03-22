
import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Sosohome_Spider(scrapy.Spider) :
    name = 'sosohome'
    start_urls = [
       'https://sosohome.co.kr/' # 메인 > 신상품 섹션 (10개)
    ]

    def parse(self, response):
        for div in response.xpath('//ul[@class="prdList grid5"]')[0].xpath('./li'):
            item = DomeScrapyItem()
            uri = 'https://sosohome.co.kr'

            thumbnail = div.xpath('./div[@class="thumbnail outline"]')
            # url_tag = thumbnail.xpath('./a/@href').get()
            url = uri # + url_tag

            img_tag = thumbnail.xpath('./a//div[@class="normal_thumb"]//img/@src').get()
            img = 'https:' + img_tag

            title = div.xpath('./div[@class="description"]//p[@class="name"]//a/text()').get()
            
            item['name'] = '소소홈'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['info'] = '11'
            item['category'] = '05' # 인테리어/소품
            yield item