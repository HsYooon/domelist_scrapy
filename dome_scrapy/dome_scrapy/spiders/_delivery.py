import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Delivery(scrapy.Spider) :
    name = 'delivery'
    start_urls = [
       'https://ad.search.naver.com/search.naver?where=ad&query=3pl&x=0&y=0', # 국내물류대행
       #'https://ad.search.naver.com/search.naver?where=ad&query=%ED%95%B4%EC%99%B8%EA%B5%AC%EB%A7%A4%EB%8C%80%ED%96%89&referenceId=hmA3%2BdprvmsssaGuPdssssssskl-245729' # 해외 구매대행
    ]

    def parse(self, response):
        cnt = 0
        for div in response.xpath('//ol[@class="lst_type"]').xpath('./li'):
            cnt+=1
            item = DomeScrapyItem()
        

            # uri = 'http://autotnb2b.com'
            url = div.xpath('./div[@class="inner"]//div[@class="url_area"]//a/text()').get()
            img = div.xpath('./div[@class="ad_thumb"]//a//img/@src').get()
            title = div.xpath('./div[@class="inner"]//a/text()').get()
            desc = div.xpath('./div[@class="inner"]//div[@class="ad_dsc"]//p/text()').get().strip()
            cate = '10'

            if url == 'http://www.js3pl.co.kr' :
                sql = f"insert into t_delivery(name,img,url,description,category,reg_dttm) values('{title}','{img}' ,'{url}','{desc}','{cate}',now());"
                print(sql) #sql문 반환
            