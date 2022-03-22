import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Schnariever_Spider(scrapy.Spider) :
    name = 'schnariever'
    
    def start_requests(self):
        url_new = 'https://schnariever.co.kr/product/list.html?cate_no=195'
        url_best = 'https://schnariever.co.kr/product/list.html?cate_no=231'

        yield scrapy.Request(url_new, self.parse_url)
        yield scrapy.Request(url_best, self.parse_url)

    
    def parse_url(self, response):
        url = response.url
        last_page = response.xpath('//*[@id="contents"]/div[3]/ol/li')[-1].xpath('./a/text()').get()
        for i in range(1, int(last_page)+1) :
            url = f'{url}&page={i}'
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
       cate_no = response.url.split('&')[0].split('=')[1]
       uri = "https://schnariever.co.kr"
       info = ''
       
       if cate_no == '195':
           info = '11'
       if cate_no == '231':
           info = '12'
       
       for div in response.xpath('//ul[@class="prdList grid4"]/li'):
            item = DomeScrapyItem()
            
            url = uri + div.xpath('./div/div[1]/div[2]/a/@href').get()
            img = 'http:' + div.xpath('./div/div[1]/div[2]/a/img/@src').get()
            title = div.xpath('./div/div[2]/strong/a/span[2]/text()').get()
            
            item['name'] = '슈나리버'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '08' # 애견
            item['info'] = info
            yield item
       