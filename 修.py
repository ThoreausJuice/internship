# 修改user表中的用户数据信息
import sqlite3

conn = sqlite3.connect('mrsoft.db')
cursor = conn.cursor()
cursor.execute('update user set name = ? where id = ?', ('MR', 1))
cursor.execute('select * from user')
result = cursor.fetchall()
print(result)
cursor.close()
conn.close()