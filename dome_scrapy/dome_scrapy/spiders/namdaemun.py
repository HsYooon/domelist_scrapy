import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Namdaemun_Spider(scrapy.Spider) :
    name = 'namdaemun'
    start_urls = [
        'http://namdaemun-mihwa.com/shop/main/index.php' # 메인 > 신상품 섹션
    ]

    def parse(self, response):

        uri = 'http://namdaemun-mihwa.com/shop'
        
        # 신상품
        for div in response.xpath('//td[@class="outline_side"]/table')[1].xpath('./tr/td'):
            item = DomeScrapyItem()
            
            url = 'http://namdaemun-mihwa.com/shop/main/index.php' 
            # url = uri + div.xpath('./div')[0].xpath('./a/@href').get()[2:] (회원접근 권한 불가)
            img = uri + div.xpath('./div')[0].xpath('./a/img/@src').get()[2:]
            title = div.xpath('./div')[1].xpath('./div')[0].xpath('./a/text()').get()

            item['name'] = '남대문미화'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '03' # 인테리어/소품
            item['info'] = '11' # 신상품
            yield item
        
        # 베스트
        for div in response.xpath('//td[@class="outline_side"]/table')[3].xpath('./tr/td'):
            item = DomeScrapyItem()
            
            url = 'http://namdaemun-mihwa.com/shop/main/index.php' 
            # url = uri + div.xpath('./div')[0].xpath('./a/@href').get()[2:] (회원접근 권한 불가)
            img = uri + div.xpath('./div')[0].xpath('./a/img/@src').get()[2:]
            title = div.xpath('./div')[1].xpath('./div')[0].xpath('./a/text()').get()

            item['name'] = '남대문미화'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '03' # 인테리어/소품
            item['info'] = '12' # 베스트
            yield item

    
        