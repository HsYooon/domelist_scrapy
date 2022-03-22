import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Goodbuying_Spider(scrapy.Spider) :
    name = 'goodbuying'
    start_urls = [
        'https://www.goodbuying.co.kr/goods/goods_main.php?sno=1' # 신상품 섹션
    ]
        
    def parse(self, response):
       
       uri = "https://www.goodbuying.co.kr"

       for div in response.xpath('//div[@class="content"]/div/div')[2].xpath('./div/div/ul/li'):
            item = DomeScrapyItem()
            
            url = uri # + div.xpath('./div/div[@class="item_photo_box"]/a/@href').get()[2:]
            img = uri + div.xpath('./div/div[@class="item_photo_box"]/a/img/@data-original').get()
            title = div.xpath('./div/div[@class="PJ_good_table"]/div/div[@class="item_tit_box"]/a/strong/text()').get()
            
            item['name'] = '굿바잉'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '12' # 신상품
            yield item

        