import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Sijangn_Spider(scrapy.Spider) :
    name = 'sijangn'
    
    def start_requests(self):
        url = 'https://www.sijangn.com'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
       uri = "https://www.sijangn.com"
       
       for div in response.xpath('//div[@class="goods_list main_wrap_12"]/div[2]/div/ul/li'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./div/div[1]/a/@href').get()[2:]
            img = uri + div.xpath('./div/div[1]/a/img/@src').get()
            title = div.xpath('./div/div[2]/div[1]/a/strong/text()').get()
            
            item['name'] = '시장엔'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '12' # 신발/잡화
            item['info'] = '11' # 신상품
            yield item