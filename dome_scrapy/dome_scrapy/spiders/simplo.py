import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Simplo_Spider(scrapy.Spider) :
    name = 'simplo'
    
    def start_requests(self):
        urls = [
        'https://www.simplo.co.kr/product/list.html?cate_no=33', # 신상품
        ]
        yield scrapy.Request(urls[0], self.parse) # 신상품
        
    def parse(self, response):
       uri = "https://www.simplo.co.kr"
       for div in response.xpath('//ul[@class="prdList grid4"]/li'):
            item = DomeScrapyItem()
            url = uri # + div.xpath('./div/div[@class="thumbnail"]/a/@href').get()
            img = div.xpath('./div/div[@class="thumbnail"]/a/img/@src').get()
            title = div.xpath('./div/div[@class="description"]/strong/a/span')[1].xpath('./text()').get()

            item['name'] = '심플로'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '11' # 의류
            item['info'] = '11' # 신상품
            yield item
       

        