# 连接数据库测试，外加查询版本

import pymssql

db = pymssql.connect(host="localhost", user="sa", password="2013cj1055", database="new", charset="CP936")
# db = pymssql.connect(host="192.168.0.211", user="sa", password="1111", database="AlarmHist", charset="CP936")

cursor = db.cursor()

if cursor:
    print("连接成功！")
db.close()