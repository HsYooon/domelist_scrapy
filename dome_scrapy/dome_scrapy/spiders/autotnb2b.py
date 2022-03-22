import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Autotnb2b_Spider(scrapy.Spider) :
    name = 'autotnb2b'
    start_urls = [
       'http://autotnb2b.com/main/index.php', # 베스트상품
    ]

    def parse(self, response):
        for div in response.xpath('//div[@class="goods_list main_wrap_1"]//div[@class="goods_list_cont goods_content_1"]//div[@class="item_basket_type"]//ul').xpath('.//li'):
            item = DomeScrapyItem()

            uri = 'http://autotnb2b.com'
            url = uri + div.xpath('./div[@class="item_cont"]//div[@class="item_photo_box"]//a/@href').get()[2:]
            img = div.xpath('./div[@class="item_cont"]//div[@class="item_photo_box"]//a//img/@src').get()
            title = div.xpath('./div[@class="item_cont"]//div[@class="item_info_cont"]//div[@class="item_tit_box"]//a//strong/text()').get()
            
            item['name'] = '오토티엔'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '06' # 자동차
            item['info'] = '12' # 신상품
            yield item