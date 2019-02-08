import dicttoxml
import os
from xml.dom.minidom import parseString

d = [20,'names',
     {'name':'Bill','age':30,'salary':2000},
     {'name':'王军','age':34,'salary':3000},
     {'name':'John','age':25,'salary':2500}]
bxml = dicttoxml.dicttoxml(d, custom_root = 'persons')

xml = bxml.decode('utf-8')
print(xml)

dom = parseString(xml)

prettyxml = dom.toprettyxml(indent = '  ')

os.makedirs('files', exist_ok = True)
f = open('files/persons.xml', 'w',encoding='utf-8')
f.write(prettyxml)
f.close()