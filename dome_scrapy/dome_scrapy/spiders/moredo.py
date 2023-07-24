import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem


class Moredo_Spider(scrapy.Spider) :
    name = 'moredo'
    start_urls = [
        'https://shop.moredo.kr/' # 메인 > 베스트 섹션
    ]

    def parse(self, response):

        uri = 'https://shop.moredo.kr'
        
        #신상품
        for div in response.xpath('//*[@id="contents"]/div[7]/ul/li'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./div/div[@class="df-prl-thumb"]/a/@href').get()
            img =  'https:' + div.xpath('./div/div[@class="df-prl-thumb"]/a/img/@src').get()
            title = div.xpath('./div/div[@class="df-prl-desc"]/div/a/span/text()').get()

            item['name'] = '모두의이불'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '03' # 인테리어/소품
            item['info'] = '11' # 신상품
            yield item

        # 신상품
        for div in response.xpath('//*[@id="contents"]/div[8]/ul/li'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./div/div[@class="df-prl-thumb"]/a/@href').get()
            img =  'https:' + div.xpath('./div/div[@class="df-prl-thumb"]/a/img/@src').get()
            title = div.xpath('./div/div[@class="df-prl-desc"]/div/a/span/text()').get()

            item['name'] = '모두의이불'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '03' # 인테리어/소품
            item['info'] = '11' # 신상품
            yield item
        
        # 베스트
        # 반응형 문제 해결
        #for div in response.xpath('//*[@id="contents"]/div[6]/div[3]'):
            #item = DomeScrapyItem()
           
            # url = 'http://namdaemun-mihwa.com/shop/main/index.php' 
            # # url = uri + div.xpath('./div')[0].xpath('./a/@href').get()[2:] (회원접근 권한 불가)
            # img = uri + div.xpath('./div')[0].xpath('./a/img/@src').get()[2:]
            # title = div.xpath('./div')[1].xpath('./div')[0].xpath('./a/text()').get()

            # item['name'] = '남대문미화'
            # item['img'] = img
            # item['url'] = url
            # item['title'] = title
            # item['category'] = '03' # 인테리어/소품
            # item['info'] = '12' # 베스트
            # yield item