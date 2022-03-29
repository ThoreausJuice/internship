# 使用pymssql访问SQL Server 数据库示例

import pprint
import pymssql

def create(new_cursor):
    new_drop='''
    IF OBJECT_ID('Class', 'U') IS NOT NULL
    DROP TABLE Class
    '''
    new_cursor.execute(new_drop)
    print("已检测到表格并删除")
    new_create = '''
    CREATE TABLE Class
    (
        class_id int CONSTRAINT PK_Class PRIMARY KEY,
        class_section varchar(max) NOT NULL,
        class_grade varchar(max) NOT NULL,
        class_no nvarchar(2) NOT NULL,
        class_room_no nvarchar(10) NOT NULL
    )
    '''
    new_cursor.execute(new_create)
    print("建表:成功！")

def add_new(new_cursor):
    # data = [(111, 'Middle_School', 'Grade_1', '1', '1-101')]
    data = [
        (111, 'Middle_School', 'Grade_1', '1', '1-101'),
        (112, 'Middle_School', 'Grade_1', '2', '1-102'),
        (113, 'Middle_School', 'Grade_1', '3', '1-103'),
        (114, 'Middle_School', 'Grade_1', '4', '1-104'),
        (121, 'Middle_School', 'Grade_1', '1', '1-203'),
        (122, 'Middle_School', 'Grade_2', '2', '1-202'),
        (123, 'Middle_School', 'Grade_2', '3', '1-205'),
        (131, 'Middle_School', 'Grade_3', '1', '1-301'),
        (132, 'Middle_School', 'Grade_3', '2', '1-302'),
        (211, 'High_School', 'Grade_1', '1', '1-101'),
    ]

    try:
        # new_add = "insert into Class values (111, '初中部', '一年级', '1', '1-101')"
        new_add = "insert into Class values (%d, %s, %s, %s, %s)"
        new_cursor.executemany(new_add, data)
        # new_cursor.execute(new_add)
        print('批量加入数据：成功！')
    except:
        print('插入：失败。')

def delete_new(new_cursor):
    new_delete = "delete from class where class_grade = %s"
    data = 'Grade_1'
    new_cursor.execute(new_delete, data)
    print('删除成功！')

def update_new(new_cursor):
    new_update = "update class set class_room_no = %s where class_id = %d"
    data = ('1-204', 122)
    new_cursor.execute(new_update, data)
    print('更新成功！')

def select_new(new_cursor):
    new_select = "select * from Class"
    new_cursor.execute(new_select)
    a = new_cursor.fetchall()
    print('查询成功！')
    for ele in a:
        print(ele)
    # pprint.pprint(a)

with pymssql.connect(host="localhost", user="sa", password="2013cj1055", database="new", charset="cp936") as new_connect:
    with new_connect.cursor() as new_cursor:
        if new_cursor:
            print("连接:成功！")
        create(new_cursor)
        
        add_new(new_cursor)
        
        delete_new(new_cursor)

        update_new(new_cursor)

        select_new(new_cursor)

        new_connect.commit()