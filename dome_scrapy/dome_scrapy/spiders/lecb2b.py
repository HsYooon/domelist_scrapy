import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Lecb2b_Spider(scrapy.Spider) :
    name = 'lecb2b'
    url= 'http://www.lecb2b.com/'
    
    def start_requests(self):
        yield scrapy.Request(self.url, self.parse)

    def parse(self, response):
       uri = "http://www.lecb2b.com"
       
       for div in response.xpath('//*[@id="mk_center"]/table')[1].xpath('./tr')[8].xpath('./td/table')[2].xpath('./tr/td[@class="lims"]'):
            item = DomeScrapyItem()
            url = uri # + div.xpath('./table/tr[1]/td/a/@href').get()
            img = uri + div.xpath('./table/tr[1]/td/a/img/@src').get()
            title = div.xpath('./table/tr[3]/td/a/font/text()').get().strip(' ')
            
            item['name'] = '레씨'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '11' # 의류
            item['info'] = '11'
            yield item
            
       for div in response.xpath('//*[@id="mk_center"]/table[2]/tr[11]/td/table[3]/tr/td[@class="lims"]'):
           item = DomeScrapyItem()
           url = uri # + div.xpath('./table/tr[1]/td/a/@href').get()
           img = uri + div.xpath('./table/tr[1]/td/a/img/@src').get()
           title = div.xpath('./table/tr[3]/td/a/font/text()').get().strip(' ')
           
           item['name'] = '레씨'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '11' # 의류
           item['info'] = '12'
           yield item