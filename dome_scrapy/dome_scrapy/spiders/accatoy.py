import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Accatoy_Spider(scrapy.Spider) :
    name = 'accatoy'
    url_new= 'https://accatoy.com/product/list.html?cate_no=49'
    #url_best = '' # 준비중 인듯
    
    def start_requests(self):
        yield scrapy.Request(self.url_new, self.parse1)
        #yield scrapy.Request(self.url_best, self.parse2)

    def parse1(self, response):
       uri = "https://accatoy.com/"
       
       for div in response.xpath('//ul[@class="prdList grid4"]/li'):
            item = DomeScrapyItem()
            
            url = uri + div.xpath('./div[@class="thumbnail"]/a/@href').get()[1:]
            img = 'https:' + div.xpath('./div[@class="thumbnail"]/a/img/@src').get()
            title = div.xpath('./div[@class="description"]/strong/a/span[2]/text()').get()
            
            item['name'] = '아카토이'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '10' # 아동/문구
            item['info'] = '11'
            yield item
