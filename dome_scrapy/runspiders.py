from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import subprocess
from time import sleep
import pymysql
from datetime import datetime
import configparser as parser

process = CrawlerProcess(get_project_settings())
#
# 주석처리 방법 
# ex) # 'domaecos'
#

spiders = [
   '2sunplanet', 'ezmarket', 'plusb2b', 'domaecos', 'airpodsredbean', 'autotnb2b', 'b2boutlet', 'b2bpet', 'b2bzoo', 'bowmall'
   , 'byramee', 'dayshouse', 'dimfac', 'dogsclub', 'domejjim', 'feelwoo', 'fromvi', 'funn', 'funtasticb2b', 'gagudome'
   , 'ggotda', 'goodbeauty', 'innovill', 'iwinwinmarket', 'jeanforce', 'jsweet', 'jystyle', 'jywholesale', 'leadersdome', 'lecb2b'
   , 'manipanda', 'mdpet', 'moonnri', 'oneplusm', 'pettory', 'pinkshop', 'plala', 'pqb2b', 'roomnoffice', 'samhoglass'
   , 'seoulbasket', 'simplo', 'soggupnoli', 'sosohome', 'specialoffer', 'sujinpet', 'twostory', 'zseller', 'accatoy', 'lalab2b'
    'comnparts', 'bbdb', 'nonda', 'gogob2b', 'choitem', 'dometopia', 'moredo', 'mroutlet', 'ahamarket', '1020bag' # 추가 예정 스크롤러
]

# 제외 스크롤러
# 'dasopoom', 'domesangin', gcol', 'hometawnggyi', 'livingchu', 'sellerz', 'sijangn', 'wehayou', 'namdaemun',
# 'goodbuying' (굿바잉) # 23.4.29 사이트 폐쇄로 삭제

# 임시 제거 스크롤러 
# jeostyle : 타임아웃  schnariever, kayu : 구조 변경
# bestket, joomengi, mongtang, dodomall
# sdmall : url 변경

# 스크롤러 
for spider in spiders:
    process.crawl(spider, domain='scrapy.org')
    sleep(1.5)

process.start() # 스크래핑이 끝날때까지 block

print("++++ Crawl Process finished ++++")

# DB 정보 
properties = parser.ConfigParser()
properties.read('./properties.ini')

config = properties['DB']
host = config['host']
user = config['user']
password = config['password']
db = config['db']
char = config['char']

# 어제까지의 데이터 삭제
answer = input("이전 데이터를 지우시겠습니다까? (Y/N)")

if str.upper(answer) == 'Y':
    today = (datetime.today().strftime("%Y%m%d"))
    # DB 연결
    connection = pymysql.connect(host = host, user= user, password = password, db = db ,charset= char ,autocommit=True)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    # 데이터 삭제
    sql = f"DELETE FROM t_domelist WHERE DATE_FORMAT(reg_dttm,'%Y%m%d') < '{today}'"
    result = cursor.execute(sql)
    print(f'=> 총 {result}개의 데이터가 삭제되었습니다.')

    # select = f"SELECT name ,count(*) as 'product count' from t_domelist group by name order by name"
    # cursor.execute(select)
    # res = cursor.fetchall()
    # for data in res:
    #     print(data)
    
    # DB 연결 해제
    connection.close()
    
