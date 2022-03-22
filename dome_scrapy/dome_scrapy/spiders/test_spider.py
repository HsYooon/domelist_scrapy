import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class TestSpider(scrapy.Spider) :
    name = 'test'
    url_new= 'http://www.lecb2b.com/'
    url_best = 'http://www.domesangin.com/goods/goods_list.php?cateCd=045'
    
    def start_requests(self):
        yield scrapy.Request(self.url_new, self.parse)
        #yield scrapy.Request(self.url_best, self.parse_url2)

    def parse_url1(self, response):
        page = response.xpath('//*[@id="contents"]/div/div/div[2]/div[5]/div/ul/li')
        url = response.url
        for i in range(1, len(page)+1):
            target_url = f'{url}&page={i}'
            yield scrapy.Request(target_url, self.parse)

    def parse_url2(self, response):
        page = response.xpath('//*[@id="contents"]/div/div/div[2]/div[4]/div/ul/li')
        url = response.url

        for i in range(1, len(page)+1):
            target_url = f'{url}&page={i}'
            yield scrapy.Request(target_url, self.parse)

    def parse(self, response):
       uri = "http://www.lecb2b.com"
       
       for div in response.xpath('//*[@id="mk_center"]/table')[1].xpath('./tr')[8].xpath('./td/table')[2].xpath('./tr/td[@class="lims"]'):
            item = DomeScrapyItem()
            url = uri + div.xpath('./table/tr[1]/td/a/@href').get()
            img = uri + div.xpath('./table/tr[1]/td/a/img/@src').get()
            title = div.xpath('./table/tr[3]/td/a/font/text()').get().strip(' ')
            print(url)
            print(img)
            print(title)
            # item['name'] = '필로우커머스'
            # item['img'] = img
            # item['url'] = url
            # item['title'] = title
            # item['category'] = '01' # 종합
            # item['info'] = '11'
            # yield item
       for div in response.xpath('//*[@id="mk_center"]/table[2]/tr[11]/td/table[3]/tr/td[@class="lims"]'):
           item = DomeScrapyItem()
           url = uri + div.xpath('./table/tr[1]/td/a/@href').get()
           img = uri + div.xpath('./table/tr[1]/td/a/img/@src').get()
           title = div.xpath('./table/tr[3]/td/a/font/text()').get()