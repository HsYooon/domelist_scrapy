import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Moonnri_Spider(scrapy.Spider) :

    name = 'moonnri'
    start_urls = [
        'http://www.moonnri.com/' # 메인 > 신상품, 베스트 
    ]

    def parse(self, response):

        uri = 'http://www.moonnri.com'
        cnt = 0
        # 신상품 섹션
        for div in response.xpath('//td[@class="lims"]'):
            item = DomeScrapyItem()
            cnt += 1
            url = uri + div.xpath('./table//tr')[0].xpath('./td/a/@href').get() # 가입페이지 이동으로 실제 db로 메인화면(uri) 삽입
            img = uri + div.xpath('./table//tr')[0].xpath('./td/a/img/@src').get()
            title = div.xpath('./table//tr')[2].xpath('./td/a/font/text()').get()
            
            # 신상품 섹션
            if cnt <= 60:
                item['name'] = '문엔리'
                item['img'] = img
                item['url'] = uri
                item['title'] = title
                item['category'] = '11' # 의류
                item['info'] = '11' # 신상품
                yield item
            else: # 베스트 섹션
                item['name'] = '문엔리'
                item['img'] = img
                item['url'] = uri
                item['title'] = title
                item['category'] = '11' # 의류
                item['info'] = '12' # 베스트
                yield item
        