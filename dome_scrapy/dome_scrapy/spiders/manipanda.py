
import scrapy
from dome_scrapy.items import DomeScrapyItem

class Manipanda_Spider(scrapy.Spider):
    
    name = 'manipanda'
    start_urls = [
        # 마니판다 > 가방 > 신상품
        'https://www.manipanda.com/category/가방new/119/' 
    ]

    def parse(self, response):

        container = response.xpath('.//div[@id="contant2"]')
    
        for div in container.css('.xans-product-normalpackage').xpath('.//li'):
            item = DomeScrapyItem()
            uri = 'https://www.manipanda.com'
            url_tag = div.css('.prdImg').xpath('@href').get()
            url = uri + url_tag

            img = 'https://' + div.css('.prdImg').xpath('.//img/@src').get()[2:]

            title = div.css('.name').xpath('.//a//span[2]/text()').get()
            
            item['name'] = '마니판다'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['info'] = '11'
            item['category'] = '12'
            yield item