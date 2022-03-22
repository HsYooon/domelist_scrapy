import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Specialoffer_Spider(scrapy.Spider) :

    #funtasticb2b > goodsDisplayWrap

    name = 'specialoffer'
    start_urls = [
       'https://specialoffer.kr/shop/new_goods_list.php', # 신상품
    ]

    def parse(self, response):
        for div in response.xpath('//div[@id="container"]//div[@class="cont_inner"]//div[@class="pr_desc wli5"]//ul').xpath('.//li'):
            item = DomeScrapyItem()

            url = div.xpath('./dl//a/@href').get()
            img = div.xpath('./dl//a//dt//img/@src').get()
            title = div.xpath('./dl//dd[@class="pname"]//div/text()').get()

            if url != None or img != None or title != None :
                item['name'] = '스페셜오퍼'
                item['img'] = img
                item['url'] = url
                item['title'] = title
                item['category'] = '01' # 종합
                item['info'] = '11' # 신상품
                yield item