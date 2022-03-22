import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Soggupnoli_Spider(scrapy.Spider) :
    name = 'soggupnoli'
    start_urls = [
        'https://www.soggupnoli.com' # 메인 > 베스트 섹션
    ]

    def parse(self, response):

        uri = 'https://www.soggupnoli.com'

        # 베스트 섹션
        for div in response.xpath('//div[@class="goods_list main_wrap_9"]/div')[1].xpath('./div/ul/li'):
            item = DomeScrapyItem()

            url = uri + div.xpath('./div/div[@class="item_photo_box"]/a/@href').get()[2:]
            img = uri + div.xpath('./div/div[@class="item_photo_box"]/a/img/@src').get()
            title = div.xpath('./div/div[@class="item_info_cont"]/div')[0].xpath('./a/strong/text()').get()

            item['name'] = '소꿉노리'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '03' # 애완
            item['info'] = '12' # 베스트
            yield item

    
        