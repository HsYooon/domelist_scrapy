import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Gagudome_Spider(scrapy.Spider) :

    name = 'gagudome'

    def start_requests(self):

        url_new = 'https://gagudome.kr/product/list.html?cate_no=234'
        url_best = 'https://gagudome.kr/product/list.html?cate_no=111'
        
        # 신상품 페이징 수
        yield scrapy.Request(url=url_new, callback=self.parse_new)
        # 베스트 페이징 수
        yield scrapy.Request(url=url_best, callback=self.parse_best)


    def parse_new(self, response):
        uri = 'https://gagudome.kr/product/list.html?cate_no=234'
        page_cnt = 0
        
        # 신상품 페이징 수
        page = response.xpath('//div[@id="contents"]/div')[4].xpath('./ol/li')[-1].xpath('./a/text()').get()
        if page != '':
            page_cnt = int(page)

        for i in range(1, page_cnt+1):
            url = uri + f'&page={i}'
            yield scrapy.Request(url=url, callback=self.parse1)
            
    
    def parse_best(self, response):
        uri = 'https://gagudome.kr/product/list.html?cate_no=111'
        page_cnt = 0
        
        # 베스트 페이징 수
        page = response.xpath('//div[@id="contents"]/div')[4].xpath('./ol/li')[-1].xpath('./a/text()').get()
        if page != '':
            page_cnt = int(page)

        for i in range(1, page_cnt+1):
            url = uri + f'&page={i}'
            yield scrapy.Request(url=url, callback=self.parse2)
        

        
    def parse1(self, response):
       item = DomeScrapyItem()
       uri = "https://gagudome.kr"
       for li in response.xpath('//ul[@class="prdList grid5"]').xpath("./li"):
           url = uri + li.xpath('./div[@class="thumbnail outline"]/a/@href').get()
           img = 'https:' + li.xpath('./div[@class="thumbnail outline"]/a/div[@class="normal_thumb"]/img/@src').get()
           title = li.xpath('./div[@class="description"]/p[@class="name"]/a/text()').get()
           
           item['name'] = '가구도매'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '03' # 인테리어/소품
           item['info'] = '11' # 신상품
           yield item
    
    def parse2(self, response):
       item = DomeScrapyItem()
       uri = "https://gagudome.kr"
       for li in response.xpath('//ul[@class="prdList grid5"]').xpath("./li"):
           url = uri + li.xpath('./div[@class="thumbnail outline"]/a/@href').get()
           img = 'https:' + li.xpath('./div[@class="thumbnail outline"]/a/div[@class="normal_thumb"]/img/@src').get()
           title = li.xpath('./div[@class="description"]/p[@class="name"]/a/text()').get()
           
           item['name'] = '가구도매'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '03' # 인테리어/소품
           item['info'] = '12' # 베스트
           yield item
            
        