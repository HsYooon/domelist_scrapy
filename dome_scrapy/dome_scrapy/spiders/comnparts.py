import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem


class Bbdb_Spider(scrapy.Spider) :
    name = 'comnparts'
    url = 'https://comnparts.co.kr/product/list.html?cate_no=23&sort_method=5#Product_ListMenu' # 베스트상품
    

    def start_requests(self):
        yield scrapy.Request(self.url, self.parse_url)
    
    def parse_url(self, response):
        url = response.url
        page = response.xpath('//*[@id="contents"]/div[4]/ol/li')
        for li in page:
            num = li.xpath('./a/text()').get()
            target_url = f'{url}&page={num}'
            yield scrapy.Request(target_url, self.parse)

    def parse(self, response):
        uri = 'https://comnparts.co.kr'
        # 베스트
        for div in response.xpath('//*[@id="contents"]/div[3]/div[3]/ul[@class="prdList grid4"]/li'):
            
            item = DomeScrapyItem()
            
            url = uri + div.xpath('./div[@class="thumbnail"]/a/@href').get()
            img =  div.xpath('./div[@class="thumbnail"]/a/div[@class="add_thumb"]/img/@src').get()
            title = div.xpath('./div[@class="description"]/p[@class="name"]/a/span[2]/text()').get()
            
            item['name'] = '컴앤파츠'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 종합
            item['info'] = '12' # 베스트
            yield item
    