import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem


class Fromvi_Spider(scrapy.Spider):
    name = 'fromvi'
    info = ['11','12']
    uri = 'https://www.fromvi.com'
    start_urls = [
       'https://www.fromvi.com/' # 메인페이지 > 신상품, 베스트 상품 (메인 페이지 외에 접근 불가) 
    ]

    def parse(self, response):
        # 신상품
        for div in response.xpath('//ul[@class="prdList grid4"]')[0].xpath('./li'):
            item = DomeScrapyItem()

            thumbMlist = div.xpath('./div[@class="thumbMlist"]')
            url = self.uri # + thumbMlist.xpath('./a/@href').get()

            img= 'https:' + thumbMlist.xpath('./a//img/@src').get()

            title = div.xpath('./div[@class="description2"]//div[@class="name"]//a//span[2]/text()').get()
            
            item['name'] = '프롬비아이'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['info'] = self.info[0]
            item['category'] = '02' # 생활
            yield item
        # 베스트
        for div in response.xpath('//ul[@class="prdList grid4"]')[1].xpath('./li'):
            item = DomeScrapyItem()
            print(div)

            thumbMlist = div.xpath('./div[@class="thumbMlist2"]')
            url = self.uri # + thumbMlist.xpath('./a/@href').get()

            img = 'https:' + thumbMlist.xpath('./a//img/@src').get()

            title = div.xpath('./div[@class="description2"]//div[@class="name"]//a//span[2]/text()').get()
            
            item['name'] = '프롬비아이'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['info'] = self.info[1]
            item['category'] = '02' # 생활
            yield item