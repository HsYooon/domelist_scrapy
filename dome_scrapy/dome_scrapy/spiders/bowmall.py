import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Bowmall_Spider(scrapy.Spider) :
    name = 'bowmall'
    start_urls = [
        'https://bowmall.co.kr/' # 신상품, 베스트
    ]
        
    def parse(self, response):
       uri = "https://bowmall.co.kr"
       
       for div in response.xpath('//div[@class="displayTabContentsContainer displayTabContentsA "]')[0].xpath('./ul/li[@class="goodsDisplayWrap"]'):
            item = DomeScrapyItem()
            url = uri + '/goods/view?no=' + div.xpath('./div/div/a/@onclick').get().split("'")[1]
            img = uri + div.xpath('./div/div/a/img/@src').get()
            title = div.xpath('./div/div/a/img/@alt').get()
                
            item['name'] = '세경카이프b2b'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '06' # 자동차
            item['info'] = '12' # 베스트
            yield item

       for div in response.xpath('//div[@class="displayTabContentsContainer displayTabContentsA "]')[1].xpath('./ul/li[@class="goodsDisplayWrap"]'):
            item = DomeScrapyItem()
            url = uri + '/goods/view?no=' + div.xpath('./div/div/a/@onclick').get().split("'")[1]
            img = uri + div.xpath('./div/div/a/img/@src').get()
            title = div.xpath('./div/div/a/img/@alt').get()
           
            item['name'] = '세경카이프b2b'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '06' # 자동차
            item['info'] = '11' #신상품
            yield item

        