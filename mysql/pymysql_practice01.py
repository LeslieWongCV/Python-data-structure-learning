# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 2:18 PM
# @Author  : Yushuo Wang
# @FileName: my_Sql.py
# @Software: PyCharm
# @Blog    ：https://lesliewongcv.github.io/


import pymysql
# connect
db = pymysql.connect(host='localhost',
                     user='root',
                     password='12345678',
                     #db='country_db', to create the db , no need to specify this arg
                     charset='utf8'
                     )
#get cursor
cursor = db.cursor()

#cteate database if doesn't exist
createdb = 'CREATE DATABASE IF NOT EXISTS country_db02'
try:
    cursor.execute(createdb)
except:
    print('already exists')

# connect database
db = pymysql.connect(host='localhost',
                     user='root',
                     password='12345678',
                     db='country_db02', # select db after creating
                     charset='utf8'
                     )
cursor = db.cursor()

# create table
createtable = "CREATE TABLE websites(id int, name char(30), url char(60), alexa int, country char(20))"

try:
    cursor.execute(createtable)
except:
    print('2')

insrt01 = " INSERT INTO websites VALUE(1,'Google','https://www.google.com/', 1, 'USA') "
insrt02 = " INSERT INTO websites VALUE(2,'淘宝','https://www.google.com/', 13, 'CN') "

multinsrt = "INSERT INTO websites VALUES (%s,%s,%s,%s,%s)" # in multi-insert: VALUES (%s, %s,  %s,  %s, %s) no ''

val = ((3,'雅虎', 'https://www.yahoo.com', 5, 'USA'),
       (4,'微博','https://www.weibo.com', 20, 'CN'),
       (5, 'Facebook', 'https://www.facebook.com', 3, 'USA'))

cursor.execute(insrt01)
cursor.execute(insrt02)
cursor.executemany(multinsrt,val)
db.commit()

# show table
select = 'SELECT * FROM websites'

try:
    cursor.execute(select)
    website_table = cursor.fetchall() #fetch all result
    #db.commit()
    for a in website_table:
        print(a)
    #print(cursor.fetchall())

except:
    db.rollback()



'''
result:
/Users/leslie/anaconda3/python.app/Contents/MacOS/python /Users/leslie/python_coding/Python_Learning/2nd_week/my_Sql.py
(1, 'Google', 'https://www.google.com/', 1, 'USA')
(2, '淘宝', 'https://www.google.com/', 13, 'CN')
(3, '雅虎', 'https://www.yahoo.com', 5, 'USA')
(4, '微博', 'https://www.weibo.com', 20, 'CN')
(5, 'Facebook', 'https://www.facebook.com', 3, 'USA')'''

