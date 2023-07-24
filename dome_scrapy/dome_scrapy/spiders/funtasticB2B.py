import scrapy
from dome_scrapy.items import DomeScrapyItem

class FuntasticB2B_Spider(scrapy.Spider) :
    name = 'funtasticb2b'

    def start_requests(self):
        yield scrapy.Request('https://funtasticb2b.co.kr/goods/catalog?perpage=160&code=00280002&popup=&iframe=', self.parse1) # 신상품
        yield scrapy.Request('https://funtasticb2b.co.kr/goods/catalog?perpage=160&display_style=lattice_a&code=00280004&popup=&iframe=', self.parse2) # 베스트

    def parse1(self, response):
        uri = "https://funtasticb2b.co.kr"
    
        for div in response.xpath('//li[@class="goodsDisplayWrap"]'):
            item = DomeScrapyItem()
        
            img_tag = div.css('.goodsDisplayImageWrap').xpath('.//img/@src').get()
            img = uri + img_tag
            # product link
            tag_a = div.css('.goodsDisplayTextWrap').xpath('.//li[2]//a/@onclick').get()
            url = uri + '/goods/view?no=' + tag_a.split("'")[1]
            # product title
            title = div.css('.goodsDisplayTextWrap').xpath('.//li[2]//a//span//text()').get()
            # item fetch
            item['name'] = '펀타스틱'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '11' # 신상품
            yield item

        
    def parse2(self, response):
        uri = "https://funtasticb2b.co.kr"
    
        for div in response.xpath('//li[@class="goodsDisplayWrap"]'):
            item = DomeScrapyItem()
        
            img_tag = div.css('.goodsDisplayImageWrap').xpath('.//img/@src').get()
            img = uri + img_tag
            # product link
            tag_a = div.css('.goodsDisplayTextWrap').xpath('.//li[2]//a/@onclick').get()
            url = uri + '/goods/view?no=' + tag_a.split("'")[1]
            # product title
            title = div.css('.goodsDisplayTextWrap').xpath('.//li[2]//a//span//text()').get()
            # item fetch
            item['name'] = '펀타스틱'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '12' # 베스트
            yield item
            