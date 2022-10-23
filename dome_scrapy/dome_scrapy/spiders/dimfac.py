import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Dimfac_Spider(scrapy.Spider) :
    name = 'dimfac'
    
    def start_requests(self):
        urls = [
        'https://www.dimfac.co.kr'
        ]
        for url in urls :
            yield scrapy.Request(url, self.parse) 
        
    def parse(self, response):
       uri = "https://www.dimfac.co.kr"

       for div in response.xpath('//div[@class="df-prl-box"]'):
           item = DomeScrapyItem()
           url = uri #+ div.xpath('./div/a/@href').get()
           img = 'https://' + div.xpath('./div[@class="df-prl-thumb"]/a/img/@src').get()[2:]
           title = div.xpath('./div[@class="df-prl-desc"]/div/a/span/text()').get()
            
           item['name'] = '딤팩'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '11' # 의류
           item['info'] = '12'
           yield item
       

        