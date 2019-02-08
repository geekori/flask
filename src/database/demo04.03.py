import xmltodict
f = open('files/products.xml','rt',encoding="utf-8")
xml = f.read()
import pprint
d = xmltodict.parse(xml)
print(d)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(d)
f.close()

