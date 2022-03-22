import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Leadersdome_Spider(scrapy.Spider) :
    name = 'leadersdome'
    
    def start_requests(self):
        urls = [
        'https://leadersdome.co.kr/index.html', # 메인 > 신상품
        ]
        yield scrapy.Request(urls[0], self.parse) # 메인 > 신상품 섹션 
        
    def parse(self, response):
       uri = "https://leadersdome.co.kr/index.html"

       for div in response.xpath('//ul[@class="prdList grid5"]/li'):
            item = DomeScrapyItem()
            url = uri # + div.xpath('./div[@class="thumbnail"]/a/@href').get()
            img = 'http:' + div.xpath('./div[@class="thumbnail"]/a/img/@src').get()
            title = div.xpath('./div[@class="description"]/span[@class="name"]/a/span')[1].xpath('./text()').get()
            
            item['name'] = '리더스도매'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '11' # 의류
            item['info'] = '11' # 베스트
            yield item
       
       for div in response.xpath('//ul[@class="prdList"]/li'):
           item = DomeScrapyItem()
           url = uri
           img = 'http:' + div.xpath('./a')[0].xpath('./img/@src').get()
           title = div.xpath('./a')[1].xpath('./div/strong[@class="name"]/text()').get()
           
           item['name'] = '리더스도매'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '11' # 의류
           item['info'] = '12' # 베스트
           yield item

        