from sqlobject import *
from sqlobject.mysql import builder
import json
mysql = 'mysql://root:12345678@localhost:3306/meituan?charset=utf8'
sqlhub.processConnection = connectionForURI(mysql,driver='pymysql')


class Person(SQLObject):
    class sqlmeta:
        table='t_persons'
    name = StringCol(length=30)
    age = IntCol()
    address = StringCol(length=30)
    salary = FloatCol()
try:    
    Person.dropTable()
except:
    pass
Person.createTable()
print('成功创建了Persons表')
person1 = Person(name='Bill', age=55,address='地球',salary=1234)
person2 = Person(name='Mike', age=65,address='月球',salary=4321)
person3 = Person(name='John', age=15,address='火星',salary=4000)
print('成功插入了3条记录')

# 修改表数据
person2.name = "李宁"
person2.address= "赛博坦"

# 查询表数据
persons = Person.selectBy(name='Bill')
print(persons[0])
print(persons[0].id) 
print(persons[0].name) 
print(persons[0].address)

def person2Dict(obj):
    return {
        'id': obj.id,
        'name': obj.name,
        'age': obj.age,
        'address':obj.address,
        'salary':obj.salary
    }

jsonStr = json.dumps(persons[0], default=person2Dict,ensure_ascii=False)
print(jsonStr)

# 删除表数据
persons[0].destroySelf()
