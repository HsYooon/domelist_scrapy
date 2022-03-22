import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Oneplusm_Spider(scrapy.Spider) :
    name = 'oneplusm'
    
    def start_requests(self):
        url = 'http://oneplusm.com/goods/goods_list2.php?cateCd=038'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
       uri = "http://oneplusm.com"
       
       # 신상품
       for div in response.xpath('//*[@id="content"]/div[1]/div/div[2]/div[3]/div/div/ul').xpath('./li'):
            item = DomeScrapyItem()
            
            url = uri + div.xpath('./div/div[1]/a/@href').get()[2:]
            img = div.xpath('./div/div[1]/a/img/@src').get()
            title = div.xpath('./div/div[2]/div[1]/a/strong/text()').get()
            
            item['name'] = '원플러스엠'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '07' # 산업
            item['info'] = '11'
            yield item
       