import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Iwinwinmarket_Spider(scrapy.Spider):
    # 윈윈마켓 
    name = 'iwinwinmarket'
    start_urls = [
       'https://www.iwinwinmarket.com/goods/goods_main.php?sno=2&pageNum=80' # 메인페이지 > 베스트 상품 섹션 (하단 페이징 처리 다시 확인후 작업) 
    ]

    def parse(self, response):

        for div in response.xpath('//div[@class="goods_list_item"]//div[@class="goods_list"]').xpath('.//li'):
            item = DomeScrapyItem()
            uri = 'https://www.iwinwinmarket.com'
            url = uri + div.xpath('./div//div[@class="item_photo_box"]//a/@href').get()[2:]

            img = div.xpath('./div//div[@class="item_photo_box"]//a//img/@src').get()
            # img url 일관성 검사
            if img.find('http') == -1:
                img = uri + img

            title = div.xpath('./div//div[@class="PJ_good_table"]//div//div[@class="item_tit_box"]//a//strong/text()').get()
         
            item['name'] = '윈윈마켓'
            item['img'] = img
            item['url'] = url
            item['title'] = title
            item['category'] = '01' # 헬스케어/뷰티
            item['info'] = '11' # 신상품
            yield item