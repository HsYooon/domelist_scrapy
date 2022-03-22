import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Domejjim_Spider(scrapy.Spider) :
    name = 'domejjim'

    def start_requests(self):
        page_cnt = 4

        url = 'http://www.domejjim.com/shop/shopbrand.html?type=Y&xcode=010&sort='

        for i in range(1, page_cnt+1):
            url = url + f'&page={i}'
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
       item = DomeScrapyItem()
       uri = "https://www.domejjim.com"
       
       for div in response.xpath('//div[@class="item-list"]/table').xpath("//td"):
           url = uri + div.xpath('./ul/div/div[@class="prd-thumb"]/a/@href').get()
           img = uri + div.xpath('./ul/div/div[@class="prd-thumb"]/a/img/@src').get()
           title = div.xpath('./ul/div/li[@class="prd_name"]/a/text()').get()

           item['name'] = '도매찜'
           item['img'] = img
           item['url'] = url
           item['title'] = title
           item['category'] = '11' # 의류
           item['info'] = '11' # 신상품
           yield item