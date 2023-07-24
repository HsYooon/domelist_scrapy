import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem


class ThreeMro_Spider(scrapy.Spider) :
    name = 'ahamarket'
    start_urls = [
        'https://ahamarket.kr/'
    ]

    def parse(self, response):
        uri = 'https://ahamarket.kr/'

         # #베스트
        for div in response.xpath('*//li[@class="pc_shop_product_design_rolling_list_item"]'):
            url =  uri
            img =  div.xpath('./a/img/@src').get()
            title = div.xpath('./a/p[@class="pc_shop_product_design_rolling_item_name"]/text()').get()
            
            item = DomeScrapyItem()
            item['name'] = '아하마켓'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '12' # 베스트
            yield item

       
        for div in response.xpath('*//li[@class="pc_shop_product_design_01_list_item"]'):
            url =  uri
            img =  div.xpath('./a/img/@src').get()
            title = div.xpath('./a/p[@class="pc_shop_product_design_01_item_name"]/text()').get()
           
            item = DomeScrapyItem()
            item['name'] = '아하마켓'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '12' # 베스트
            yield item
        