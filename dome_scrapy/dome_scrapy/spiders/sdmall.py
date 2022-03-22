import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Sdmall_Spider(scrapy.Spider) :
    name = 'sdmall'
    start_urls = [
        'https://b2b.sdmall.co.kr/search/?isnew=Y' 
    ]
        
    def parse(self, response):
       item = DomeScrapyItem()
       uri = "https://b2b.sdmall.co.kr"
       
       for div in response.xpath('//ul[@class="cateprdul2 searchUl"]').xpath("./li"):
           url = uri + div.xpath('./div[@class="imgWrap"]/img/@onclick').get().split("'")[1]
           img = div.xpath('./div[@class="imgWrap"]/img/@src').get()
           title = div.xpath('./div')[2].xpath('./text()').get()

           item['name'] = 'sdmall'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '11' # 의류
           item['info'] = '11' # 신상품
           yield item