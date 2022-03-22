import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Seoulbasket_Spider(scrapy.Spider) :
    name = 'seoulbasket'
    start_urls = [
        'http://seoulbasket.com/product/list.html?cate_no=48' # 신상품 
    ]
        
    def parse(self, response):
       uri = "http://seoulbasket.com"
       for div in response.xpath('//ul[@class="prdList grid4"]/li'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./div[@class="thumbnail"]/a/@href').get()
            img = "http:" + div.xpath('./div[@class="thumbnail"]/a/img/@src').get()
            title = div.xpath('./div[@class="description"]/strong/a/span')[1].xpath('./text()').get()
            
            item['name'] = '서울등공예'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '03' # 인테리어/소품
            item['info'] = '11'
            yield item
       

        