import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class TestSpider(scrapy.Spider) :
    name = '퍼줌넷'
    
    def start_requests(self):
        url = 'http://www.perzoom.co.kr/shop/shopbrand.html?xcode=073&type=P'
        yield scrapy.Request(url, self.url_parse)
    
    def url_parse(self, response) :
        limit = 2 # 2 페이지까지 scrap
        page = response.xpath('//*[@id="productClass"]/div[2]/div[2]/ol/li[10]/a/text()').get()
        
        if limit < int(page):
            for i in range(1,limit+1):
                url = f'http://www.perzoom.co.kr/shop/shopbrand.html?type=P&xcode=073&sort=&page={i}'
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
       uri = "http://pink-shop.co.kr"
       print("called")
       for div in response.xpath('//div[@class="prd-list pdt30"]/table//tr'):
            item = DomeScrapyItem()
            # img = div.xpath('./div/p[@class="prdImg"]/a/img/@src').get()
            # title = div.xpath('./div/p[@class="name"]/strong/a/span')[1].xpath('./text()').get()
            print(div.get())
            # item['name'] = '핑크샵'
            # item['img'] = img
            # item['url'] = url
            # item['title'] = title
            # item['category'] = '11' # 종합
            # item['info'] = '12'
            # yield item