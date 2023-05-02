import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Gagudome_Spider(scrapy.Spider) :

    name = 'gagudome'

    def start_requests(self):

        url_new = 'https://gagudome.kr/category/%EC%8B%A0%EC%83%81%ED%92%88/234/'
        url_best = 'https://gagudome.kr/category/BEST-TOP-100/111/'
        
        # 신상품 페이징 수
        #yield scrapy.Request(url=url_new, callback=self.parse_new)
        # 베스트 페이징 수
        yield scrapy.Request(url=url_best, callback=self.parse_best)


    def parse_new(self, response):
        url = 'https://gagudome.kr/category/%EC%8B%A0%EC%83%81%ED%92%88/234'
        page_cnt = 0
        
        # 신상품 페이징 수
        
        page = response.xpath('//*[@id="contents"]/div[7]/div/div[2]/div[2]/ol/li')[-1].xpath('./a/text()').get()
        if page != '':
            page_cnt = int(page)

        for i in range(1, page_cnt+1):
            url = url + f'/?page={i}'
            yield scrapy.Request(url=url, callback=self.parse1)
            
    
    def parse_best(self, response):
        uri = 'https://gagudome.kr/category/BEST-TOP-100/111'
        page_cnt = 0
        
        # 베스트 페이징 수
        page = response.xpath('//*[@id="contents"]/div[7]/div/div[2]/div[2]/ol/li')[-1].xpath('./a/text()').get()
        if page != '':
            page_cnt = int(page)

        for i in range(1, page_cnt+1):
            url = uri + f'/?page={i}'
            yield scrapy.Request(url=url, callback=self.parse2)
        

        
    def parse1(self, response):
       item = DomeScrapyItem()
       uri = "https://gagudome.kr"
       for li in response.xpath('//*[@id="contents"]/div[7]/div/div[2]/div[1]/ul').xpath('./li'):
           url = uri + li.xpath('./div/div[@class="thumbnail"]/a/@href').get()
           img = 'https:' + li.xpath('./div/div[@class="thumbnail"]/a/img/@src').get()
           title = li.xpath('./div/div[@class="description"]/div/a/span[2]/text()').get()
           
           item['name'] = '친절한 공룡'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '03' # 인테리어/소품
           item['info'] = '11' # 신상품
           yield item
    
    def parse2(self, response):
       item = DomeScrapyItem()
       uri = "https://gagudome.kr"
       for li in response.xpath('//*[@id="contents"]/div[7]/div/div[2]/div[1]/ul').xpath("./li"):
           url = uri + li.xpath('./div/div[@class="thumbnail"]/a/@href').get()
           img = 'https:' + li.xpath('./div/div[@class="thumbnail"]/a/img/@src').get()
           title = li.xpath('./div/div[@class="description"]/div/a/span[2]/text()').get()
           
           item['name'] = '친절한 공룡'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '03' # 인테리어/소품
           item['info'] = '12' # 베스트
           yield item
            
        