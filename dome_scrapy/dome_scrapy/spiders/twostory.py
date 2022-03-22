import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Twostory_Spider(scrapy.Spider) :
    name = 'twostory'
    start_urls = [
        'http://www.twostory.co.kr/' # 신상품, 베스트
    ]
        
    def parse(self, response):
       uri = "http://www.twostory.co.kr"
       cnt = 0
       for div in response.xpath('//td[@class="lims"]'):
            item = DomeScrapyItem()
            cnt += 1
            info = '11' # 신상품
            
            url = uri + div.xpath('./table/tr')[0].xpath('./td/a/@href').get()
            img = uri + div.xpath('./table/tr')[0].xpath('./td/a/img/@src').get()
            title = div.xpath('./table/tr')[2].xpath('./td/a/font/text()').get()
            
            if cnt > 20 :
                info = '12'
                
            item['name'] = '투스토리'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = info
            yield item

        