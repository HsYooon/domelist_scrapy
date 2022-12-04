import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class TestSpider(scrapy.Spider) :
    name = 'test'
    url_new= 'https://accatoy.com/product/list.html?cate_no=49'
    #url_best = 'https://www.lalab2b.com/goods/goods_list.php?cateCd=009&sort=orderCnt+desc%2Cg.regDt+desc&pageNum=40'
    
    def start_requests(self):
        yield scrapy.Request(self.url_new, self.parse1)
        #yield scrapy.Request(self.url_best, self.parse)

    # def parse_url1(self, response):
    #     page = response.xpath('//*[@id="contents"]/div/div/div[2]/div[5]/div/ul/li')
    #     url = response.url
    #     for i in range(1, len(page)+1):
    #         target_url = f'{url}&page={i}'
    #         yield scrapy.Request(target_url, self.parse)

    # def parse_url2(self, response):
    #     page = response.xpath('//*[@id="contents"]/div/div/div[2]/div[4]/div/ul/li')
    #     url = response.url

    #     for i in range(1, len(page)+1):
    #         target_url = f'{url}&page={i}'
    #         yield scrapy.Request(target_url, self.parse)

    def parse1(self, response):
       uri = "https://accatoy.com/"
       
       for div in response.xpath('//ul[@class="prdList grid4"]/li'):
            item = DomeScrapyItem()
            
            url = uri + div.xpath('./div[@class="thumbnail"]/a/@href').get()[1:]
            img = 'https:' + div.xpath('./div[@class="thumbnail"]/a/img/@src').get()
            title = div.xpath('./div[@class="description"]/strong/a/span[2]/text()').get()
            print(title)
            
            
            item['name'] = '아카토이'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '10' # 아동/문구
            item['info'] = '11'
            yield item
    #    for div in response.xpath('//*[@id="mk_center"]/table[2]/tr[11]/td/table[3]/tr/td[@class="lims"]'):
    #        item = DomeScrapyItem()
    #        url = uri + div.xpath('./table/tr[1]/td/a/@href').get()
    #        img = uri + div.xpath('./table/tr[1]/td/a/img/@src').get()
    #        title = div.xpath('./table/tr[3]/td/a/font/text()').get()
