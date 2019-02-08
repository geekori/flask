import json
class Product:
    def __init__(self, name,price,count):
        self.name = name
        self.price = price
        self.count = count
def product2Dict(obj):
    return {
        'name': obj.name,
        'price': obj.price,
        'count': obj.count
    }
product = Product('特斯拉',1000000,20)
jsonStr = json.dumps(product, default=product2Dict,ensure_ascii=False)
print(jsonStr)

