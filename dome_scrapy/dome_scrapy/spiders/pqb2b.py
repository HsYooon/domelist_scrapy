import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Pqb2b_Spider(scrapy.Spider) :
    name = 'pqb2b'
    info = ['11','12'] # 11: 신상품 12: 베스트 

    def start_requests(self):
        #yield scrapy.Request('https://pqb2b.co.kr/product/list.html?cate_no=150&sort_method=5&page=1', self.parse) # 메인 > 신상품 섹션 
        #yield scrapy.Request('https://pqb2b.co.kr/product/list.html?cate_no=150&sort_method=5&page=2', self.parse),
        #yield scrapy.Request('https://pqb2b.co.kr/product/list.html?cate_no=150&sort_method=5&page=3', self.parse)
        #yield scrapy.Request('https://pqb2b.co.kr/product/list.html?cate_no=151&page=1', self.parse2), # 인기상품 100
        yield scrapy.Request('https://pqb2b.co.kr/product/list.html?cate_no=151&page=2', self.parse2)

    def parse(self, response):
        for div in response.xpath('//ul[@class="prdList grid4"]').xpath('./li'):
            
            item = DomeScrapyItem()
            uri = 'https://pqb2b.co.kr'

            thumbnail = div.xpath('./div[@class="thumbnail outline"]')
            url_tag = thumbnail.xpath('./a/@href').get()
            url = uri + url_tag

            img_tag = thumbnail.xpath('./a//div[@class="add_thumb"]//img/@src').get()
            img = 'https:' + img_tag

            title = div.xpath('./div[@class="description"]//p[@class="name"]//a/text()').get()
            
            item['name'] = 'pqb2b'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['info'] = self.info[0]
            item['category'] = '01' # 종합
            yield item

    def parse2(self, response):
        for div in response.xpath('//ul[@class="prdList grid4"]').xpath('./li'):
            item = DomeScrapyItem()
            uri = 'https://pqb2b.co.kr'

            thumbnail = div.xpath('./div[@class="thumbnail outline"]')
            url_tag = thumbnail.xpath('./a/@href').get()
            url = uri + url_tag

            img_tag = thumbnail.xpath('./a//div[@class="add_thumb"]//img/@src').get()
            img = 'https:' + img_tag

            title = div.xpath('./div[@class="description"]//p[@class="name"]//a/text()').get()
            
            item['name'] = 'pqb2b'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['info'] = self.info[1]
            item['category'] = '01' # 종합
            yield item