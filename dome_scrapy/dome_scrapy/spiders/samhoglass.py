import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Samhoglass_Spider(scrapy.Spider) :
    name = 'samhoglass'
    start_urls = [
        'http://www.samhoglass.co.kr' 
    ]
        
    def parse(self, response):
       item = DomeScrapyItem()
       uri = "http://www.samhoglass.co.kr"
       
       for div in response.xpath('//div[@id="w2aDesign_contents"]/div/div/div')[5].xpath("./ul/li"):
           url = uri + div.xpath('./div/div[@class="thumbnail"]/a/@href').get()
           img = 'https:' + div.xpath('./div/div[@class="thumbnail"]/a/img/@src').get()
           title = div.xpath('./div/div[@class="description"]/strong/a/span/text()').get()

           item['name'] = '삼호유리'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '03' # 의류
           item['info'] = '11' # 신상품
           yield item

       for div in response.xpath('//div[@id="w2aDesign_contents"]/div/div/div')[7].xpath("./ul/li"):
           url = uri + div.xpath('./div/div[@class="thumbnail"]/a/@href').get()
           img = 'https:' + div.xpath('./div/div[@class="thumbnail"]/a/img/@src').get()
           title = div.xpath('./div/div[@class="description"]/strong/a/span/text()').get()
      
           item['name'] = '삼호유리'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '03' # 의류
           item['info'] = '12' # 베스트
           yield item

        