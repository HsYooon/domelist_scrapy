import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Funn_Spider(scrapy.Spider) :
    name = 'funn'
    start_urls = [
        'http://b2b.funn.co.kr/goods/BestGoods.asp?page=1&listsize=90' # 베스트 90개
    ]
        
    def parse(self, response):
       uri = "http://b2b.funn.co.kr"

       for div in response.xpath('//form[@id="RGFrm"]/ul[@class="__itemlist _null"]/li'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./a/@href').get()
            img = div.xpath('./a/img/@src').get()
            title = div.xpath('./a/span[@class="sbj"]/text()').get()

            item['name'] = '펀앤'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '12' # 신상품
            yield item

        