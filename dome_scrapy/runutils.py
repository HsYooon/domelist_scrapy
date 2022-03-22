from time import sleep
import pymysql
from datetime import datetime
import configparser as parser

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
print("원하는 작업을 선택하세요.")
print("[1] 지난 날짜 데이터 삭제")
print("[2] 특정 데이터 삭제")
print("[3] 상품 개수 현황")
answer = input("번호를 입력하세요 : ")

if answer != '':
    num = str(answer)
    # DB 연결
    connection = pymysql.connect(host = host, user= user, password = password, db = db ,charset= char ,autocommit=True)
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    if num == '1':
        env = '개발'
        if host == '203.245.41.222':
            env = '운영'

        a = input(f"현제 DB는 [{env}]입니다. 삭제하시겠습니까?(Y/N)")
        if str.upper(a) == 'Y':
            today = (datetime.today().strftime("%Y%m%d"))
            sql = f"DELETE FROM t_domelist WHERE DATE_FORMAT(reg_dttm,'%Y%m%d') < '{today}'"
            result = cursor.execute(sql)
            print(f'=> 총 {result}개의 데이터가 삭제되었습니다.')
    
    elif num == '2':
        sql = f"SELECT min(name) as 'name' from t_domelist group by name order by name"
        cursor.execute(sql)
        res = cursor.fetchall()

        print("-[name]-------------")
        for data in res:
            name = data["name"]
            print(name)
        print("--------------------")

        a = input(f"삭제할 [name]을 입력하세요:")
        sql = f"DELETE FROM t_domelist WHERE name = '{a}'"

        if a != '':
            result = cursor.execute(sql)
            print(f'=> 총 {result}개의 데이터가 삭제되었습니다.')

        
    
    elif num == '3':
        sql = f"SELECT name ,count(*) as 'count' from t_domelist group by name order by name"
        cursor.execute(sql)
        res = cursor.fetchall()
        for data in res:
            name = data["name"]
            count = data["count"]
            print(f'[{name}] 상품수 : {data["count"]}')
    
    # DB 연결 해제
    connection.close()