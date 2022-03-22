import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Domaecos_Spider(scrapy.Spider) :

    name = 'domaecos'
    start_urls = [
       'http://www.domaecos.com/shop/main/index.php' # 메인페이지 > 신상품 섹션 
    ]

    def parse(self, response):

        for div in response.xpath('//div[@class="prd_list"]')[1].xpath('./table//td[@align="center"]'):
            item = DomeScrapyItem()

            #url = div.xpath('./div[@class="thumb"]//a/@href').get()
            uri = 'https://www.domaecos.com/shop'
            img = uri + div.xpath('./div[@class="thumb"]//a//img/@src').get()[2:]
            title = div.xpath('./div[@class="name"]//a//span/@title').get()
         
            item['name'] = '도매코스'
            item['img'] = img
            item['url'] = uri #로그인 페이지로 이동 -> 메인이동 고정
            item['title'] = title
            item['info'] = '11' # 신상품
            item['category'] = '05' # 헬스케어/뷰티
            yield item