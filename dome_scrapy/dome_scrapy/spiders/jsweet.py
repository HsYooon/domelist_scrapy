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
       
       for div in response.xpath('//*[@id="contents"]/div[5]/ul/li'):
           url = uri # + div.xpath('./div/center')[0].xpath('./a/@href').get()
           img = 'http:' + div.xpath('./div/div[1]/a/img/@src').get()
           title = div.xpath('./div/div[3]/div/a/span/text()').get()
           
           item['name'] = '제이스윗'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '11' # 의류
           item['info'] = '11' # 신상품
           yield item

       for div in response.xpath('//*[@id="contents"]/div[6]/ul/li'):
           url = uri # + div.xpath('./div/center')[0].xpath('./a/@href').get()
           img = 'http:' + div.xpath('./div/div[1]/a/img/@src').get()
           title = div.xpath('./div/div[3]/div/a/span/text()').get()
           
           item['name'] = '제이스윗'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '11' # 의류
           item['info'] = '12' # 베스트
           yield item
        