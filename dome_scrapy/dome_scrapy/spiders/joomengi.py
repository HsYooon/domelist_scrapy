import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Joomenfi_Spider(scrapy.Spider) :
    name = 'joomengi'
    
    def start_requests(self):
        url = 'http://www.joomengi.com'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
       uri = "http://www.joomengi.com"
       
       for div in response.xpath('//ul[@class="prdList grid4"]/li'):
            item = DomeScrapyItem()
            url = uri # + div.xpath('./div/div[1]/a/@href').get()
            img = 'http:' + div.xpath('./div/div[1]/a/img/@src').get()
            title = div.xpath('./div/div[4]/div/p/a/span/text()').get()
            
            item['name'] = '신고메고'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '12' # 종합
            item['info'] = '12'
            yield item