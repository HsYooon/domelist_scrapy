import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Jsweet_Spider(scrapy.Spider) :
    name = 'jsweet'
    start_urls = [
        'http://www.jsweet.co.kr' # 메인 > 베스트 섹션
    ]
        
    def parse(self, response):
       item = DomeScrapyItem()
       uri = "http://www.jsweet.co.kr"
       
       for div in response.xpath('//ul[@class="prdList column4"]')[0].xpath("./li"):
           url = uri # + div.xpath('./div/center')[0].xpath('./a/@href').get()
           img = 'http:' + div.xpath('./div/center')[0].xpath('./a/img/@src').get()
           title = div.xpath('./div/center')[1].xpath('./a/span/text()').get()

           item['name'] = '제이스윗'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '11' # 의류
           item['info'] = '11' # 신상품
           yield item

       for div in response.xpath('//ul[@class="prdList column4"]')[1].xpath("./li"):
           url = uri # + div.xpath('./div/center')[0].xpath('./a/@href').get()
           img = 'http:' + div.xpath('./div/center')[0].xpath('./a/img/@src').get()
           title = div.xpath('./div/center')[1].xpath('./a/span/text()').get()

           item['name'] = '제이스윗'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '11' # 의류
           item['info'] = '12' # 베스트
           yield item
        