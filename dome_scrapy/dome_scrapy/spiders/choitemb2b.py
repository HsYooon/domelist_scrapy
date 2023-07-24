import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class ChoitemB2b_Spider(scrapy.Spider) :
    name = 'choitem'

    def start_requests(self):
        yield scrapy.Request('https://choitemb2b.com/product/list.html?cate_no=56&page=1', self.parse1) # 신상품
        yield scrapy.Request('https://choitemb2b.com/product/list.html?cate_no=56&page=2', self.parse1) # 신상품
        yield scrapy.Request('https://choitemb2b.com/product/list.html?cate_no=56&page=3', self.parse1) # 신상품
        #yield scrapy.Request('https://choitemb2b.com/product/list.html?cate_no=54', self.parse2) # 베스트
        
        
    def parse1(self, response):
       for div in response.xpath('//*[@id="contents"]/div[4]/div[2]/ul/li'):
            item = DomeScrapyItem()
            url = 'https://choitemb2b.com' + div.xpath('./div[1]/a/@href').get()
            img = 'https:' + div.xpath('./div[1]/a/div/img/@src').get()
            title = div.xpath('./div[2]/p[@class="name"]/a/text()').get().strip()

            item['name'] = '초이템'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '11' # 신상품
            yield item


    def parse2(self, response):
       for div in response.xpath('//*[@id="contents"]/div[4]/div[2]/ul/li'):
            item = DomeScrapyItem()
            url = 'https://choitemb2b.com' + div.xpath('./div[1]/a/@href').get()
            img = 'https:' + div.xpath('./div[1]/a/div/img/@src').get()
            title = div.xpath('./div[2]/p[@class="name"]/a/text()').get().strip()

            item['name'] = '초이템'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '12' # 베스트
            yield item
        