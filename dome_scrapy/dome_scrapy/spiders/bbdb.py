import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem


class Bbdb_Spider(scrapy.Spider) :
    name = 'bbdb'
    start_urls = [
        'http://bbdb.co.kr/' # 메인 > 
    ]

    def parse(self, response):

        uri = 'http://bbdb.co.kr'
        
        #신상품
        for div in response.xpath('//*[@id="contents"]/div[2]/div[2]/div/div[2]/div/div[2]//ul/li'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./div/div[1]/a/@href').get()[2:]
            img =  div.xpath('./div/div[1]/a/img/@data-original').get()
            title = div.xpath('./div/div[2]/div[2]/a/strong/text()').get()
            
            item['name'] = '바비디부'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '03' # 인테리어/소품
            item['info'] = '11' # 신상품
            yield item
        
        # 베스트
        for div in response.xpath('//*[@id="contents"]/div[2]/div[4]/div[1]/div[2]/div/ul/li'):
            item = DomeScrapyItem()
        
            url = uri + div.xpath('./div/div[1]/a/@href').get()[2:]
            img =  div.xpath('./div/div[1]/a/img/@data-original').get()
            title = div.xpath('./div/div[2]/div[2]/a/strong/text()').get()

            item['name'] = '바비디부'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '03' # 인테리어/소품
            item['info'] = '12' # 베스트
            yield item