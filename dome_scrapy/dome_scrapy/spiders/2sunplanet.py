import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Sunplanet_Spider(scrapy.Spider) :
    name = '2sunplanet'
    
    def start_requests(self):
        url = 'https://2sunplanet.com/'  # 메인 > 신상품 섹션
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
       uri = "https://2sunplanet.com"
       
       for div in response.xpath('//div[@class="shop-item _shop_item"]'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./div[1]/a/@href').get()
            img = div.xpath('./div[1]/a/img/@data-original').get()
            title = div.xpath('./div[2]/div[1]/h2/a/text()').get()
            
            item['name'] = '투썬플래닛'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '02' # 생활
            item['info'] = '11'
            yield item