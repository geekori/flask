import json
import dicttoxml
f = open('files/products.json','r',encoding='utf-8')
jsonStr = f.read()
d = json.loads(jsonStr)
print(d)
xmlStr = dicttoxml.dicttoxml(d).decode('utf-8')
print(xmlStr)
f.close()
