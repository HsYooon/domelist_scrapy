import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Roomnoffice_Spider(scrapy.Spider) :

    name = 'roomnoffice'

    def start_requests(self):

        url_new = 'https://www.xn--jt2by0pl8b7va956c.kr/product/list.html?cate_no=101'
        url_best = 'https://www.xn--jt2by0pl8b7va956c.kr/product/list.html?cate_no=25'
        
        # 신상품 url
        yield scrapy.Request(url=url_new, callback=self.parse_new)
        # 베스트 url
        yield scrapy.Request(url=url_best, callback=self.parse_best)


    def parse_new(self, response):
        uri = 'https://www.xn--jt2by0pl8b7va956c.kr/product/list.html?cate_no=101'
        page_cnt = 0
        
        # 신상품 페이징 수 조회
        page = response.xpath('//div[@id="contents"]/div')[2].xpath('./ol/li')[-1].xpath('./a/text()').get()
        if page != '':
            page_cnt = int(page)

        for i in range(1, page_cnt+1):
            url = uri + f'&page={i}'
            print(url)
            yield scrapy.Request(url=url, callback=self.parse1)
            
    
    def parse_best(self, response):
        uri = 'https://www.xn--jt2by0pl8b7va956c.kr/product/list.html?cate_no=25'
        page_cnt = 0
        
        # 베스트상품 페이징 수 조회
        page = response.xpath('//div[@id="contents"]/div')[2].xpath('./ol/li')[-1].xpath('./a/text()').get()
        if page != '':
            page_cnt = int(page)

        for i in range(1, page_cnt+1):
            url = uri + f'&page={i}'
            print(url)
            yield scrapy.Request(url=url, callback=self.parse2)
        

        
    def parse1(self, response):
       item = DomeScrapyItem()
       
       uri = "https://www.xn--jt2by0pl8b7va956c.kr"
       exception = ['E-MONEY 상품권' , '배송비결제']

       for li in response.xpath('//ul[@class="prdList grid5"]').xpath("./li"):
           url = uri + li.xpath('./div[@class="thumbnail"]/div[@class="prdImg"]/a/@href').get()
           img = 'https://' + li.xpath('./div[@class="thumbnail"]/div[@class="prdImg"]/a/img/@src').get()[2:]
           title = li.xpath('./div[@class="description"]/strong[@class="name"]/a/span')[1].xpath('./text()').get()
           
           if title in exception:
               continue
           item['name'] = '룸앤오피스'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '03' # 인테리어/소품
           item['info'] = '11' # 신상품
           yield item

    def parse2(self, response):
       item = DomeScrapyItem()
       
       uri = "https://www.xn--jt2by0pl8b7va956c.kr"
       exception = ['E-MONEY 상품권' , '배송비결제']

       for li in response.xpath('//ul[@class="prdList grid5"]').xpath("./li"):
           url = uri + li.xpath('./div[@class="thumbnail"]/div[@class="prdImg"]/a/@href').get()
           img = 'https://' + li.xpath('./div[@class="thumbnail"]/div[@class="prdImg"]/a/img/@src').get()[2:]
           title = li.xpath('./div[@class="description"]/strong[@class="name"]/a/span')[1].xpath('./text()').get()
           
           if title in exception:
               continue
           item['name'] = '룸앤오피스'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '03' # 인테리어/소품
           item['info'] = '12' # 신상품
           yield item


        