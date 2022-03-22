import scrapy
from dome_scrapy.items import DomeScrapyItem

class Kayu_Spider(scrapy.Spider) :
    # 카유니아 
    name = 'kayu' 
    start_urls = [
       'http://www.kayu.co.kr/goods/goods_list.php?page=1&cateCd=015&sort=date&pageNum=40', #도매사입제품 > 최신순 > 40개씩 
       'http://www.kayu.co.kr/goods/goods_list.php?page=2&cateCd=015&sort=date&pageNum=40'
    ]

    def parse(self, response):
        for div in response.css('.item_gallery_type').xpath('.//li'):
            item = DomeScrapyItem()
            uri = 'http://www.kayu.co.kr'
            # url_tag = div.css('.item_photo_box').xpath('.//a/@href').get()[2:]
            url = uri # + url_tag
            img = div.css('.item_photo_box').xpath('.//img/@src').get()
            title = div.css('.item_info_cont').css('.item_tit_box').xpath('.//strong/text()').get()
            
            item['name'] = '카유니아'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['info'] = '11'
            item['category'] = '05'
            yield item