import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Gcol_Spider(scrapy.Spider) :
    name = 'gcol'
    
    def start_requests(self):
        url = 'http://www.gcol.co.kr/'
        yield scrapy.Request(url, self.parse) # 메인 > outer, top, bottom, skirt, dress, homewear
        
        
    def parse(self, response):
       uri = "http://www.gcol.co.kr/"
       
       for div in response.xpath('//div[@class="box rolling_1"]/table/tr/td/table'):
            item = DomeScrapyItem()
            
            url = uri # + div.xpath('./tr/td/table')[0].xpath('./tr/td/a/@href').get()
            img = uri + div.xpath('./tr/td/table')[0].xpath('./tr/td/a/img/@src').get()[1:]
            title = div.xpath('./tr/td/table')[2].xpath('./tr/td/a/text()').get()
            
            item['name'] = '지컬렉션'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '11' # 의류
            item['info'] = '12'
            yield item

        