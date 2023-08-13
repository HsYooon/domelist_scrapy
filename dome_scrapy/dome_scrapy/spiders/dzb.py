import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem
from playwright.async_api import async_playwright

class DZB_Spider(scrapy.Spider) :
    name = 'dzb'
    start_urls = [
        'https://www.dzb.co.kr/' # 메인 > Top100
    ]

    def parse(self, response):

        uri = 'https://www.dzb.co.kr'

        # 신상품 섹션
        for div in response.xpath('//*[@id="content"]/div[4]/div/div/div/div/div/ul/li'):
            item = DomeScrapyItem()

            url = uri + div.xpath('./div/div[@class="thumbnail"]/a/@href').get()[2:]
            img = div.xpath('./div/div[@class="thumbnail"]/a/img/@src').get()
            title = div.xpath('./div/div[@class="txt"]/a/strong/text()').get()

            item['name'] = 'dzb'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '11' # 신상품
            yield item

    
        