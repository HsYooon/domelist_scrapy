import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Bowmall_Spider(scrapy.Spider) :
    name = 'bowmall'

    def start_requests(self):
        yield scrapy.Request('https://bowmall.co.kr', self.parse1) # 신상품, 베스트 
        yield scrapy.Request('https://bowmall.co.kr/goods/catalog?code=0001', self.parse2) # 인기상품 100
        yield scrapy.Request('https://bowmall.co.kr/goods/catalog?code=0003', self.parse2) # 카테고리
        yield scrapy.Request('https://bowmall.co.kr/goods/catalog?code=0006', self.parse2) # 카테고리
        yield scrapy.Request('https://bowmall.co.kr/goods/catalog?code=0009', self.parse2) # 카테고리 70
        yield scrapy.Request('https://bowmall.co.kr/goods/catalog?code=0010', self.parse2) # 카테고리
        
        
    def parse1(self, response):
       uri = "https://bowmall.co.kr"
       
       for div in response.xpath('//div[@class="displayTabContentsContainer displayTabContentsA "]')[0].xpath('./ul/li[@class="goodsDisplayWrap"]'):
            item = DomeScrapyItem()
            url = uri + '/goods/view?no=' + div.xpath('./div/div/a/@onclick').get().split("'")[1]
            img = uri + div.xpath('./div/div/a/img/@src').get()
            title = div.xpath('./div/div/a/img/@alt').get()
        
            item['name'] = '세경카이프b2b'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '06' # 자동차
            item['info'] = '12' # 베스트
            yield item

       for div in response.xpath('//div[@class="displayTabContentsContainer displayTabContentsA "]')[1].xpath('./ul/li[@class="goodsDisplayWrap"]'):
            item = DomeScrapyItem()
            url = uri + '/goods/view?no=' + div.xpath('./div/div/a/@onclick').get().split("'")[1]
            img = uri + div.xpath('./div/div/a/img/@src').get()
            title = div.xpath('./div/div/a/img/@alt').get()
            
            item['name'] = '세경카이프b2b'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '06' # 자동차
            item['info'] = '11' #신상품
            yield item

    def parse2(self, response):
        uri = "https://bowmall.co.kr"
        
        for div in response.xpath('//div[@class="displayTabContentsContainer displayTabContentsA "]')[0].xpath('./ul/li[@class="goodsDisplayWrap"]'):
            item = DomeScrapyItem()
            url = uri + '/goods/view?no=' + div.xpath('./div/div/a/@onclick').get().split("'")[1]
            img = uri + div.xpath('./div/div/a/img/@src').get()
            title = div.xpath('./div/div/a/img/@alt').get()

            item['name'] = '세경카이프b2b'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '06' # 자동차
            item['info'] = '12' # 베스트
            yield item
        