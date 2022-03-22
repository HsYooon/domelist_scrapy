import scrapy
from dome_scrapy.items import DomeScrapyItem

class FuntasticB2B_Spider(scrapy.Spider) :
    name = 'funtasticb2b'
    start_urls = [
        'https://funtasticb2b.co.kr/goods/catalog?page=1&sort=newly&code=0010',
        'https://funtasticb2b.co.kr/goods/catalog?page=2&sort=newly&code=0010',
        'https://funtasticb2b.co.kr/goods/catalog?page=3&sort=newly&code=0010'
    ]

    def parse(self, response):
        uri = "https://funtasticb2b.co.kr"
    
        for div in response.css('.goodsDisplayItemWrap'):
            item = DomeScrapyItem()
        
            img_tag = div.css('.goodsDisplayImageWrap').xpath('.//img/@src').get()
            img = uri + img_tag 
            # product link
            tag_a = div.css('.goodsDisplayTextWrap').xpath('.//li[2]//a/@onclick').get()
            url = uri + '/goods/view?no=' + tag_a.split("'")[1]
            # product title
            title = div.css('.goodsDisplayTextWrap').xpath('.//li[2]//a//span//text()').get()
            # item fetch
            item['name'] = 'funtasticB2B'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01'
            item['info'] = '11'
            yield item