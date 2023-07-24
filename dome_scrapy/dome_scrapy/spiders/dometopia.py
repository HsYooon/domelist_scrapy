import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Dometopia_Spider(scrapy.Spider) :
    name = 'dometopia'
    start_urls = [
        'https://www.dometopia.com/main/index' # 메인
    ]
        
    def parse(self, response):
       uri = 'https://www.dometopia.com'

       for div in response.xpath('//*[@class="goodsroll best"][1]/div[2]/table//td[@class="goodsWrap"]'):
            item = DomeScrapyItem()

            url = uri + div.xpath('./dl/dt/span/a/@href').get()
            img = div.xpath('./dl/dt/span/a/img/@src').get()
            title = div.xpath('./dl/dd[@class="goodsDisplayTitle"]/div/a/h6/text()').get()
            
            item['name'] = '도매토피아'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '12' # 베스트
            yield item

       for div in response.xpath('//*[@class="goodsroll best"][2]/div[2]/table//td[@class="goodsWrap"]'):
            item = DomeScrapyItem()

            url = uri + div.xpath('./dl/dt/span/a/@href').get()
            img = div.xpath('./dl/dt/span/a/img/@src').get()
            title = div.xpath('./dl/dd[@class="goodsDisplayTitle"]/div/a/h6/text()').get()
            
            item['name'] = '도매토피아'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '11' # 신상품
            yield item

        