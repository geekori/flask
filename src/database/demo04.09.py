import sqlite3
import os

dbPath = 'data.sqlite'
if not os.path.exists(dbPath):
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()
    c.execute('''CREATE TABLE persons
       (id INT PRIMARY KEY     NOT NULL,
       name           TEXT    NOT NULL,
       age            INT     NOT NULL,
       address        CHAR(50),
       salary         REAL);''')


    conn.commit()
    conn.close()
    print('创建数据成功')



conn = sqlite3.connect(dbPath)
c = conn.cursor()
c.execute('delete from persons')
c.execute("INSERT INTO persons (id,name,age,address,salary) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");
c.execute("INSERT INTO persons (id,name,age,address,salary) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

c.execute("INSERT INTO persons (id,name,age,address,salary) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

c.execute("INSERT INTO persons (id,name,age,address,salary) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");    
conn.commit()

print('插入数据成功')

persons = c.execute("select name,age,address,salary from persons order by age")
print(type(persons))
result = []
for person in persons:
    value = {}
    value['name'] = person[0]
    value['age'] = person[1]
    value['address'] = person[2]
    result.append(value)
conn.close() 
print(type(result))
print(result)

import json
resultStr = json.dumps(result)
print(type(resultStr))
print(resultStr)


