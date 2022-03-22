import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Domesangin_Spider(scrapy.Spider) :
    name = 'domesangin'
    url_new= 'http://www.domesangin.com/goods/goods_list.php?cateCd=038'
    url_best = 'http://www.domesangin.com/goods/goods_list.php?cateCd=045'
    
    def start_requests(self):
        yield scrapy.Request(self.url_new, self.parse_url1)
        yield scrapy.Request(self.url_best, self.parse_url2)

    def parse_url1(self, response):
        page = response.xpath('//*[@id="contents"]/div/div/div[2]/div[5]/div/ul/li')
        url = response.url
        for i in range(1, len(page)+1):
            target_url = f'{url}&page={i}'
            yield scrapy.Request(target_url, self.parse)

    def parse_url2(self, response):
        page = response.xpath('//*[@id="contents"]/div/div/div[2]/div[4]/div/ul/li')
        url = response.url

        for i in range(1, len(page)+1):
            target_url = f'{url}&page={i}'
            yield scrapy.Request(target_url, self.parse)

    def parse(self, response):
       uri = "http://www.domesangin.com"
       
       for div in response.xpath('//div[@class="goods_list_item"]/div[@class="goods_list"]/div/div/ul').xpath('./li'):
            item = DomeScrapyItem()
            info = ''
            request_url = response.url.split('&')[0]
            
            if request_url == self.url_new:
                info = '11'
            if request_url == self.url_best:
                info = '12'

            url = uri + div.xpath('./div/div[1]/a/@href').get()
            img = uri + div.xpath('./div/div[1]/a/img/@src').get()
            title = div.xpath('./div/div[2]/div[1]/a/strong/text()').get()
            
            item['name'] = '도매상인'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '09' # 디지털/가전
            item['info'] = info
            yield item
       