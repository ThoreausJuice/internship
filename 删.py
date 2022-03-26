# 删除用户数据信息

import sqlite3

conn = sqlite3.connect('mrsoft.db')
cursor = conn.cursor()
cursor.execute('delete from user where id = ?', (1,))
cursor.execute('select * from user')
result = cursor.fetchall()
print(result)
cursor.close()
conn.close()