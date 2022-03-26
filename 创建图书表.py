import pymysql

db = pymysql.connect(host="localhost", user="root", password="2013cj1055", database="mr")
cursor = db.cursor()
cursor.execute("drop table if exists books")
sql = """
create table books(
    id int(8) not null auto_increment,
    name varchar(50) not null,
    category varchar(50) not null,
    price decimal(10,2) default null,
    publish_time date default null,
    primary key (id)
)   engine=myisam auto_increment=1 default charset=utf8;
"""
cursor.execute(sql)
db.close()