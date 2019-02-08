import json
class Product:
    def __init__(self, d):
        self.__dict__ = d

f = open('files/products.json','r', encoding='utf-8')
jsonStr = f.read()

products = json.loads(jsonStr, object_hook=Product)
for product in products:     
    print('name', '=', product.name)
    print('price', '=', product.price)
    print('count', '=', product.count)   
f.close()

def product2Dict(product):   
    return {
        'name': product.name,
        'price': product.price,
        'count': product.count
        }

jsonStr = json.dumps(products, default=product2Dict,ensure_ascii=False)
print(jsonStr)
