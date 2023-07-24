import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem


class Gabang_Spider(scrapy.Spider) :
    name = '1020bag'
    start_urls = [
        'https://www.1020bag.com/'
    ]

    def parse(self, response):
        uri = 'https://www.1020bag.com/'

        #신상품
        for div in response.xpath('//*[@id="contents"]/div/div[5]/div/div/div[2]/div[1]/ul/li'):
            
            url = uri
            img = div.xpath('./div/div[1]/a/img/@src').get()
            title = div.xpath('./div/div[2]/div[1]/a/strong/text()').get()
            
            item = DomeScrapyItem()
            item['name'] = '가방쟁이'
            item['img'] = img
            item['url'] = uri
            item['title'] = title
            item['category'] = '12' # 신발/잡화
            item['info'] = '11' # 신상품
            yield item
        