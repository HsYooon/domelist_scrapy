import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Lalab2b_Spider(scrapy.Spider) :
    name = 'lalab2b'
    url_new= 'https://www.lalab2b.com/goods/goods_list.php?page=3&cateCd=009&sort=g.regDt%20desc&pageNum=40' # 페이지 조정해야함 사진 안나와서 3page부터 함
    url_best = 'https://www.lalab2b.com/goods/goods_list.php?cateCd=009&sort=orderCnt+desc%2Cg.regDt+desc&pageNum=40'
    
    def start_requests(self):
        yield scrapy.Request(self.url_new, self.parse1)
        yield scrapy.Request(self.url_best, self.parse2)

    def parse1(self, response):
       uri = "https://www.lalab2b.com/"
       
       for div in response.xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[1]/div/ul/li'):
            item = DomeScrapyItem()
            
            url = uri + div.xpath('./div/div[@class="thumbnail"]/a/@href').get()[2:]
            img = div.xpath('./div/div[@class="thumbnail"]/a/img/@src').get()
            title = div.xpath('./div/div[@class="txt"]/a/strong/text()').get()
            
            item['name'] = '라라팬시'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '10' # 아동/문구
            item['info'] = '11'
            yield item

    def parse2(self, response):
       uri = "https://www.lalab2b.com/"
       
       for div in response.xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[1]/div/ul/li'):
            item = DomeScrapyItem()
            
            url = uri + div.xpath('./div/div[@class="thumbnail"]/a/@href').get()[2:]
            img = div.xpath('./div/div[@class="thumbnail"]/a/img/@src').get()
            title = div.xpath('./div/div[@class="txt"]/a/strong/text()').get()
            
            item['name'] = '라라팬시'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '10' # 아동/문구
            item['info'] = '12'
            yield item
