from pymysql import *
import json
def connectDB():
    db=connect("127.0.0.1","root","12345678","meituan",charset='utf8')
    return db
db = connectDB()
print(type(db))
def createTable(db):    
    cursor=db.cursor()    
    sql='''CREATE TABLE persons
       (id INT PRIMARY KEY     NOT NULL,
       name           TEXT    NOT NULL,
       age            INT     NOT NULL,
       address        CHAR(50),
       salary         REAL);'''
    try:   
        cursor.execute(sql)
         # 提交到数据库执行
        db.commit()
        return True
    except:
        # 如果发生错误则回滚
        db.rollback()
    return False


def insertRecords(db):   
    cursor=db.cursor()    
    try:   
        cursor.execute('DELETE FROM persons')
        cursor.execute("INSERT INTO persons (id,name,age,address,salary) \
          VALUES (1, 'Paul', 32, 'California', 20000.00 )");
        cursor.execute("INSERT INTO persons (id,name,age,address,salary) \
          VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
    
        cursor.execute("INSERT INTO persons (id,name,age,address,salary) \
          VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
    
        cursor.execute("INSERT INTO persons (id,name,age,address,salary) \
          VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )"); 
        # 提交到数据库执行
        db.commit()
        return True
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        db.rollback()
    return False
def selectRecords(db):
    cursor=db.cursor()  
    sql='SELECT name,age,salary FROM persons ORDER BY age DESC'
    cursor.execute(sql)
    results=cursor.fetchall()
    print(results)
    fields = ['name','age','salary']
    records=[]
    for row in results:
        records.append(dict(zip(fields,row)))
    return json.dumps(records)    
    
    

if createTable(db):
    print('成功创建persons表')
else:
    print('persons表已经存在')

if insertRecords(db):
    print('成功插入记录')
else:
    print('插入记录失败')
print(selectRecords(db))
db.close()