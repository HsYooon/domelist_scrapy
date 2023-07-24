import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem


class Mroutlet_Spider(scrapy.Spider) :
    name = 'mroutlet'
    start_urls = [
        'http://mroutlet.cafe24.com/' # 메인 
    ]

    def parse(self, response):

        uri = 'http://mroutlet.cafe24.com/'
        
        #신상품
        for div in response.xpath('//*[@id="contents"]/div[3]/ul/li'):
            item = DomeScrapyItem()

            url = uri + div.xpath('./div/a/@href').get()
            img =  'https:' + div.xpath('./div/a/img/@src').get()
            title = div.xpath('./div/p[@class="name"]/a/span/text()').get()
           
            item['name'] = '미래아울렛'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '11' # 신상품
            yield item
        
        # 베스트
        for div in response.xpath('//*[@id="contents"]/div[4]/ul/li'):
            item = DomeScrapyItem()

            url = uri + div.xpath('./div/a/@href').get()
            img =  'https:' + div.xpath('./div/a/img/@src').get()
            title = div.xpath('./div/p[@class="name"]/a/span/text()').get()
        
            item['name'] = '미래아울렛'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '12' # 베스트
            yield item