#!/usr/bin/python3

# 数据读写测试

def process(string):
    'just a print'
    print('Processing: ', string)

f = open('test.txt')

while True :
    line = f.readline()
    if not line:
        break
    process(line)

f.close()
print(process.__doc__)