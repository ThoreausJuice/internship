# 实现数据库的连接、建表、增删改查

import pymssql

def create(new_cursor):
    new_drop='''
    IF OBJECT_ID('books', 'U') IS NOT NULL
    DROP TABLE books
    '''
    new_cursor.execute(new_drop)
    print("已检测到表格并删除")
    new_create = """
    create table books(
    id  int IDENTITY(1,1) not null,
    name varchar(50) not null,
    category varchar(50) not null,
    price decimal(10,2) default null,
    publish_time date default null,
    primary key (id))
    """
    new_cursor.execute(new_create)
    print("建表:成功！")

def add(new_cursor):
    data = [('零基础学Python', 'Python', '79.80', '2018-5-20')]
    # data = [("零基础学Python", 'Python', '79.80', '2018-5-20'),
    #     ("Python从入门到项目实践", 'Python', '99.80', '2019-6-18'),
    #     ("PyQt5从入门到实践", 'Python', '69.80', '2020-5-21'),
    #     ("OpenCV从入门到实践", 'Python', '69.80', '2020-5-21'),
    #     ("Python算法从入门到实践", 'Python', '69.80', '2020-5-21')
    #     ]
    new_add='insert into books(name, category, price, publish_time) values (%s,%s,%s,%s)'
    # try:
    new_cursor.executemany(new_add, data)
    new_connect.commit()
    print("增加数据:成功！")
    # except:
        # new_connect.rollback()
        # print("增加数据:失败！")

with pymssql.connect(host="localhost", user="sa", password="2013cj1055", database="new", charset="CP936") as new_connect:
    with new_connect.cursor() as new_cursor:
        if new_cursor:
            print("连接:成功！")
        create(new_cursor)
        # add(new_cursor)