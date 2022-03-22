import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class B2bzoo_Spider(scrapy.Spider) :
    name = 'b2bzoo'
    url_new = 'http://b2bzoo.co.kr/promotion/top_event_01.html'
    url_best = 'http://b2bzoo.co.kr/promotion/top_event_02.html'

    def start_requests(self):
        yield scrapy.Request(self.url_new, self.parse)
        yield scrapy.Request(self.url_best, self.parse)


    def parse(self, response):
       uri = "http://b2bzoo.co.kr"
       info = ''

       if response.url == self.url_new:
           info = '11'
       if response.url == self.url_best:
           info = '12'
       
       for div in response.xpath('//ul[@class="prdList"]/li'):
            item = DomeScrapyItem()
            
            url = uri #+ div.xpath('./a[1]/@href').get()
            img = 'http:' + div.xpath('./a[1]/img/@src').get()
            title = div.xpath('./a[2]/span/text()').get()
            
            item['name'] = '비투비쥬'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '08' # 애견
            item['info'] = info
            yield item
       