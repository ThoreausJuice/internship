# 连接数据库测试，外加查询版本，navicat成功

import pymysql

db = pymysql.connect(host="localhost", user="root", password="2013cj1055", database="mr")

cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
cursor.execute("select version()")
data = cursor.fetchone()
print("database version : %s " % data)
db.close()