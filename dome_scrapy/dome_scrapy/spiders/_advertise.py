import scrapy
from bs4 import BeautifulSoup
from dome_scrapy.items import DomeScrapyItem

class Delivery(scrapy.Spider) :
    name = 'advertise'
    start_urls = [
        #"https://ad.search.naver.com/search.naver?where=ad&query=%EA%B2%80%EC%83%89%EA%B4%91%EA%B3%A0&referenceId=hBpyPwprvTVssLSXbBVsssssslC-204490",
       # DA광고
#'https://ad.search.naver.com/search.naver?where=ad&query=DA%EA%B4%91%EA%B3%A0&x=0&y=0',


#쇼핑광고

#'https://ad.search.naver.com/search.naver?where=ad&query=%EC%87%BC%ED%95%91%EA%B4%91%EA%B3%A0&x=0&y=0',


#체험단리뷰

'https://ad.search.naver.com/search.naver?where=ad&query=%EC%B2%B4%ED%97%98%EB%8B%A8%EB%A6%AC%EB%B7%B0&x=0&y=0'

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
            cate = '15'
            cnt += 1
            
            sql = f"insert into t_delivery(name,img,url,description,category,reg_dttm) values('{title}','{img}' ,'{url}','{desc}','{cate}',now());"
            print(sql) #sql문 반환