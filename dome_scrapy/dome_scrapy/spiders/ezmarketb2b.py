import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class EzmarketB2B_Spider(scrapy.Spider) :
    name = 'ezmarket'
    url_new= 'https://ezmarketb2b.com/goods/catalog?code=0019'
    url_best = 'https://ezmarketb2b.com/goods/catalog?code=0026'
    
    def start_requests(self):
        yield scrapy.Request(self.url_new, self.parse)
        yield scrapy.Request(self.url_best, self.parse2)

    def parse(self, response):
       uri = "https://ezmarketb2b.com"
       
       for div in response.xpath('//div[@class="displayTabContentsContainer displayTabContentsA "]').xpath('./ul/li[@class="goodsDisplayWrap"]'):
            item = DomeScrapyItem()
            url = uri + '/goods/view?no=' + div.xpath('./div/div/a/@onclick').get().split("'")[1]
            img = uri + div.xpath('./div/div/a/img/@src').get()
            title = div.xpath('./div/ul/li[1]/a/span/text()').get()
            
            item['name'] = '이지마켓'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '11' # 신상품
            yield item

    def parse2(self, response):
       uri = "https://ezmarketb2b.com"
       
       for div in response.xpath('//div[@class="displayTabContentsContainer displayTabContentsA "]').xpath('./ul/li[@class="goodsDisplayWrap"]'):
            item = DomeScrapyItem()
            url = uri + '/goods/view?no=' + div.xpath('./div/div/a/@onclick').get().split("'")[1]
            img = uri + div.xpath('./div/div/a/img/@src').get()
            title = div.xpath('./div/ul/li[1]/a/span/text()').get()

            item['name'] = '이지마켓'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '12' # 신상품
            yield item