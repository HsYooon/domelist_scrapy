import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Sellerz_Spider(scrapy.Spider) :
    name = 'sellerz'
    start_urls = [
        'http://www.sellerz.kr/' # 베스트
    ]
        
    def parse(self, response):
       uri = "http://www.sellerz.kr/"
       for div in response.xpath('//div[@class="newGoodsItem main_item_title"]/div[@class="swiper-container"]/div/div'):
            item = DomeScrapyItem()
            url = uri 
            img = uri + div.xpath('./div/ul/li')[0].xpath('./a/img/@src').get()
            title = div.xpath('./div/ul/li')[1].xpath('./a/text()').get()
            
            item['name'] = '셀러즈'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '12' # 신상품
            yield item

        