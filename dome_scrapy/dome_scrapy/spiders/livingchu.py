import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Livingchu_Spider(scrapy.Spider) :
    name = 'livingchu'
    start_urls = [
        'http://livingchu.com/main/index.php' # 신상품 섹션
    ]
        
    def parse(self, response):
       
       uri = "http://livingchu.com"

       for div in response.xpath('//div[@class="main_box3"]')[1].xpath('./div/div')[1].xpath('./div/ul/li'):
            item = DomeScrapyItem()
            if div.xpath('@class').get() == 'item_soldout':
                continue
            url = uri # + div.xpath('./div/div[@class="item_photo_box"]/a/@href').get()[2:]
            img = uri + div.xpath('./div/div[@class="item_photo_box"]/a/img/@data-original').get()
            title = div.xpath('./div/div[@class="item_info_cont"]/div[@class="item_tit_box"]/a/strong/text()').get()
           
            item['name'] = '리빙츄'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '11' # 신상품
            yield item

       for div in response.xpath('//div[@class="main_box4"]')[0].xpath('./div/div')[1].xpath('./div/ul/li'):
            item = DomeScrapyItem()
            if div.xpath('@class').get() == 'item_soldout':
                continue
            url = uri # + div.xpath('./div/div[@class="item_photo_box"]/a/@href').get()[2:]
            img = uri + div.xpath('./div/div[@class="item_photo_box"]/a/img/@data-original').get()
            title = div.xpath('./div/div[@class="item_info_cont"]/div[@class="item_tit_box"]/a/strong/text()').get()
           
            item['name'] = '리빙츄'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '12' # 신상품
            yield item

        