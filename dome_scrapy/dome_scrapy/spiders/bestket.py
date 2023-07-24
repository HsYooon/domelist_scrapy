import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem


class Bestket_Spider(scrapy.Spider) :
    name = 'bestket'
    start_urls = [
        'http://b2b.bestket.com/index.html'
    ]

    def parse(self, response):
        uri = 'http://b2b.bestket.com/index.html'
        
        images = []
        urls =[]
        titles = []

        #신상품
        for div in response.xpath('//div[@class="list_div_d"]'):
            img = div.xpath('./a/img/@src').get()
            images.append(img)

        for div in response.xpath('//div[@class="list_div_d2"]'):
            # url = div.xpath('./div[1]/a/@href').get() => 상품 존재하지 않는다고 뜸. url 을 메인 페이지로 변경 (23.7.9)
            title = div.xpath('./div[1]/a/p/text()').get()
            titles.append(title)
        
        if(len(images) == len(titles)):
            for i in range(len(images)):
                item = DomeScrapyItem()

                item['name'] = '베스트켓'
                item['img'] = images[i]
                item['url'] = uri
                item['title'] = titles[i]
                item['category'] = '01' # 종합
                item['info'] = '11' # 신상품
                yield item
        