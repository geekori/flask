import xmltodict
from pymongo import *
Client = MongoClient()
db = Client.data
products = db.products 
products.delete_many({'price':{'$gt':0}})
f = open('products.xml','rt',encoding="utf-8")
xml = f.read()
f.close()
import pprint
d = xmltodict.parse(xml)
print(d)
productList = d['root']['products']['product']


for product in productList:
    product['price'] = int(product['price'])
    productId = products.insert_one(product).inserted_id
    print(productId)


for product in products.find({'price':{'$gt':10000}}):
    print(product)
