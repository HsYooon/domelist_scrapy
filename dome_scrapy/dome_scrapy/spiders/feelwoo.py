import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Feelwoo_spider(scrapy.Spider) :
    name = 'feelwoo'
    url_new= 'https://www.feelwoo.com/goods/goods_search.php?reSearchKeyword%5B%5D=&reSearchKey%5B%5D=goodsNm&sort=g.regDt+desc&pageNum=100&key=goodsNm&keyword=&cateGoods%5B%5D=&cateGoods%5B%5D=&cateGoods%5B%5D=&cateGoods%5B%5D=&goodsPrice%5B%5D=&goodsPrice%5B%5D='
    url_best = 'https://www.feelwoo.com/goods/goods_search.php?reSearchKeyword%5B%5D=&reSearchKey%5B%5D=goodsNm&sort=orderCnt+desc%2Cg.regDt+desc&pageNum=100&key=goodsNm&keyword=&cateGoods%5B%5D=&cateGoods%5B%5D=&cateGoods%5B%5D=&cateGoods%5B%5D=&goodsPrice%5B%5D=&goodsPrice%5B%5D='
    
    def start_requests(self):
        yield scrapy.Request(self.url_new, self.parse_new)
        yield scrapy.Request(self.url_best, self.parse_best)


    def parse_new(self, response):
       uri = "https://www.feelwoo.com"
       
       
       for div in response.xpath('//*[@id="content"]/div/div/div/div[1]/div/div/ul').xpath('./li'):
            item = DomeScrapyItem()
            
            url = uri + div.xpath('./div/div[1]/a/@href').get()[2:]
            img = div.xpath('./div/div[1]/a/img/@src').get()
            title = div.xpath('./div/div[2]/a/strong/text()').get()
            
            item['name'] = '필로우커머스'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '11'
            yield item

    def parse_best(self, response):
       uri = "https://www.feelwoo.com"
       
       
       for div in response.xpath('//*[@id="content"]/div/div/div/div[1]/div/div/ul').xpath('./li'):
            item = DomeScrapyItem()
            
            url = uri + div.xpath('./div/div[1]/a/@href').get()[2:]
            img = div.xpath('./div/div[1]/a/img/@src').get()
            title = div.xpath('./div/div[2]/a/strong/text()').get()
            
            item['name'] = '필로우커머스'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '12'
            yield item
       