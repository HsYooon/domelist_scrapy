import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Ggotda_Spider(scrapy.Spider) :
    name = 'ggotda'
    start_urls = [
       'https://www.ggotda.com/product/list.html?cate_no=74' # 메인페이지 > 신상품 섹션 
    ]

    def parse(self, response):
        for div in response.xpath('//ul[@class="prdList grid3"]').xpath('./li'):
            item = DomeScrapyItem()
            uri = 'https://ggotda.com'

            common = div.xpath('./div[@class="thumbnail"]//div[@class="prdImg"]')
            url = uri + common.xpath('./a/@href').get()

            img = 'https://' + common.xpath('./a//img[1]/@src').get()[2:]

            title = div.xpath('./div[@class="description"]//strong[@class="name"]//span[2]/text()').get()
         
            item['name'] = '꽃다'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '05' # 헬스케어/뷰티
            item['info'] = '11' # 신상품
            yield item