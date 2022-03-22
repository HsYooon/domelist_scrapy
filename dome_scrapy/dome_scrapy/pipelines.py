# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import configparser as parser

class DomeScrapyPipeline:
    # DB 정보 
    properties = parser.ConfigParser()
    properties.read('./properties.ini')

    config = properties['DB']
    host = config['host']
    user = config['user']
    password = config['password']
    db = config['db']
    char = config['char']

    def __init__(self):
        print("DB Connection Start =========================>")
        self.connection = pymysql.connect(host = self.host, user= self.user, password = self.password, db = self.db ,charset= self.char ,autocommit=True)
        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
        sql = f"insert into t_domelist(name, img, url, title, category, info, reg_dttm) values('{item['name']}','{item['img']}','{item['url']}','{item['title']}','{item['category']}','{item['info']}',now())"
        print(f'SQL Execute =====================> {sql}')
        self.cursor.execute(sql)
        return item
