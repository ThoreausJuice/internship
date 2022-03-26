# 使用3种方式查询用户数据信息
import sqlite3

conn = sqlite3.connect('mrsoft.db')
cursor = conn.cursor()
# cursor.execute("select * from user")
cursor.execute("select * from user where id > ? and id < ?", (1,3))

# result1 = cursor.fetchone()
# print(result1)

# result2 = cursor.fetchmany(2)
# print(result2)

result3 = cursor.fetchall()
print(result3)


cursor.close()
conn.close()