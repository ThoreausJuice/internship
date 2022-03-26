#!/usr/bin/python3

# 数据库支持测试

import sqlite3

# 转换函数
def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        # print('0')
        return float(value)

# 连接数据库文件
conn = sqlite3.connect('food.db')
# 游标
curs = conn.cursor()

curs.execute('''
CREATE TABLE food (
id      TEXT    PRIMARY KEY,
desc    TEXT,
water   FLOAT,
kcal    FLOAT,
protein FLOAT,
fat     FLOAT,
ash     FLOAT,
carbs   FLOAT,
fiber   FLAOT,
sugar   FLOAT
)
''')

query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'

field_count = 10

for line in open('A.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query, vals)

conn.commit()
conn.close()