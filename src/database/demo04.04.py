import json

data = {
    'name' : 'Bill',
    'company' : 'Microsoft',
    'age' : 34
}

jsonStr = json.dumps(data)
print(type(jsonStr))
print(jsonStr)

data = json.loads(jsonStr)
print(type(data))
print(data)
s = '''
{
    'name' : 'Bill',
    'company' : 'Microsoft',
    'age' : 34
}
'''
data = eval(s)
print(type(data))
print(data)
print(data['company'])

f = open('files/products.json','r',encoding='utf-8')
jsonStr = f.read()
json1 = eval(jsonStr)
json2 = json.loads(jsonStr)
print(json1)
print(json2)
print(json2[0]['name'])
f.close()