# 新增用户数据信息
import sqlite3

conn = sqlite3.connect('mrsoft.db')
cursor = conn.cursor()
cursor.execute("insert into user (id, name) values ('1', 'MRSOFT')")
cursor.execute("insert into user (id, name) values ('2', 'Andy')")
cursor.execute("insert into user (id, name) values ('3', '明日科技小助手')")
cursor.close()
conn.commit()
conn.close()