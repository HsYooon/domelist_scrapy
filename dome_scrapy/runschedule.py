import schedule
import time
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import subprocess
from time import sleep
import pymysql
from datetime import datetime
import configparser as parser

def job():

    # DB 정보 
    properties = parser.ConfigParser()
    properties.read('./properties.ini')

    config = properties['DB']
    host = config['host']
    user = config['user']
    password = config['password']
    db = config['db']
    char = config['char']

    today = (datetime.today().strftime("%Y%m%d"))

    # DB 연결
    connection = pymysql.connect(host = host, user= user, password = password, db = db ,charset= char ,autocommit=True)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    print("dd")
    # Auto_increament 확인 
    sql = f"select max(id) max from t_domelist"
    cursor.execute(sql)
    res = cursor.fetchall()
    for data in res:
        value = data["max"]
        if value > 10000:
            sql = f"DELETE FROM t_domelist where 1=1"
            cursor.execute(sql)
            result = cursor.execute("ALTER TABLE t_domelist AUTO_INCREMENT = 1")
            print(result)

    process = CrawlerProcess(get_project_settings())
    spiders = [
        'ezmarket',
        'plusb2b',
        'domaecos',
        '2sunplanet',
        'airpodsredbean',
        'autotnb2b',
        'b2boutlet',
        'b2bpet',
        'b2bzoo',
        'bowmall',
        'byramee',
        'dasopoom',
        'dayshouse',
        'dimfac',
        'dodomall',
        'dogsclub',
        'domejjim',
        'domesangin',
        'feelwoo',
        'fromvi',
        'funn',
        'funtasticb2b',
        'gagudome',
        'gcol',
        'ggotda',
        'goodbeauty',
        'goodbuying',
        'hometawnggyi',
        'innovill',
        'iwinwinmarket',
        'jeanforce',
        'jeostyle',
        'joomengi',
        'jsweet',
        'jystyle',
        'jywholesale',
        'kayu',
        'leadersdome',
        'lecb2b',
        'livingchu',
        'manipanda',
        'mdpet',
        'mongtang',
        'moonnri',
        'namdaemun',
        'oneplusm',
        'pettory',
        'pinkshop',
        'plala',
        'pqb2b',
        'roomnoffice',
        'samhoglass',
        'schnariever',
        'sdmall',
        'sellerz',
        'seoulbasket',
        'sijangn',
        'simplo',
        'soggupnoli',
        'sosohome',
        'specialoffer',
        'sujinpet',
        'twostory',
        'wehayou',
        'zseller'
    ]
    
    # 스크롤러 
    for spider in spiders:
        process.crawl(spider, domain='scrapy.org')
        sleep(1.5)

    process.start() # the script will block here until the crawling is finished

    print("++++ Crawl Process finished ++++")

    # 데이터 삭제
    sql = f"DELETE FROM t_domelist WHERE DATE_FORMAT(reg_dttm,'%Y%m%d') < '{today}'"
    result = cursor.execute(sql)
    print(f'=> 총 {result}개의 데이터가 삭제되었습니다.')

    # DB 연결 해제
    connection.close()



if __name__ == '__main__':
    schedule.every().day.at("22:00").do(job) # 11:41분에 동작
    schedule.every().day.at("22:05").do(exit) # 프로그램 종료 시간
 
    # 스케쥴을 유지
    while True:
        schedule.run_pending()
        time.sleep(1)