import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

# 조은뷰티
class Goodbeauty_Spider(scrapy.Spider):
    name = 'goodbeauty'
    info = ['11','12'] # 11: 신상품 12: 베스트 

    def start_requests(self):
        yield scrapy.Request('http://goodbeauty.co.kr/', self.parse) # 메인 > 신상품 섹션 
        yield scrapy.Request('http://goodbeauty.co.kr/product/list.html?cate_no=127', self.parse2) # 인기상품 100

    def parse(self, response):
        for div in response.xpath('//ul[@class="prdList grid3"]').xpath('./li'):
            item = DomeScrapyItem()

            uri = 'http://goodbeauty.co.kr'
            url_tag = div.xpath('./div[@class="thumbnail outline"]//a/@href').get()
            url = uri + url_tag

            img_tag = div.xpath('./div[@class="thumbnail outline"]//a//div[@class="normal_thumb"]//img/@src').get()
            img = 'http:' + img_tag
            
            title = div.xpath('./div[@class="description"]//p//a/text()').get()
       
            item['name'] = '조은뷰티'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['info'] = self.info[0]
            item['category'] = '05' # 헬스케어/뷰티
            yield item

    def parse2(self, response):
        for div in response.xpath('//ul[@class="prdList grid4"]').xpath('./li'):
            item = DomeScrapyItem()

            uri = 'http://goodbeauty.co.kr'
            url_tag = div.xpath('./div[@class="thumbnail outline"]//a/@href').get()
            url = uri + url_tag

            img_tag = div.xpath('./div[@class="thumbnail outline"]//a//div[@class="normal_thumb"]//img/@src').get()
            img = 'http:' + img_tag
            
            title = div.xpath('./div[@class="description"]//p//a/text()').get()
       
            item['name'] = '조은뷰티'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['info'] = self.info[1]
            item['category'] = '05' # 헬스케어/뷰티
            yield item