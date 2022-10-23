import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Domaecos_Spider(scrapy.Spider) :

    name = 'domaecos'
    start_urls = [
        'https://www.domaecos.com/shop/goods/goods_search.php?page=1&&searched=Y&sort=b.goodsno+desc&page_num=100&skey=all',
        'https://www.domaecos.com/shop/goods/goods_search.php?page=2&&searched=Y&sort=b.goodsno+desc&page_num=100&skey=all'
         # 최신등록 & 수정된 상품 200
    ]

    def parse(self, response):

        for div in response.xpath('//*[@id="form"]/table/tr[6]/td/table//td[@align="center"]'):
            item = DomeScrapyItem()
            
            uri = 'https://www.domaecos.com/shop'
            img = uri + div.xpath('./div[@class="thumb"]//a//img/@src').get()[2:]
            title = div.xpath('./div[@class="name"]//a//span/@title').get()
            
            item['name'] = '도매코스'
            item['img'] = img
            item['url'] = uri #로그인 페이지로 이동 -> 메인이동 고정
            item['title'] = title
            item['info'] = '11' # 신상품
            item['category'] = '05' # 헬스케어/뷰티
            yield item