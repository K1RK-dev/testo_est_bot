import json
from urllib import request, parse
from config import FP_TOKEN


class FrontPadAPI:
    def __init__(self):
        pass

    def send_order(self, data):
        data = parse.urlencode(data, True).encode()
        req = request.Request('https://app.frontpad.ru/api/index.php?new_order',
                              data=data,
                              method="POST",
                              headers={"Content-Type": "application/x-www-form-urlencoded"})
        resp = request.urlopen(req)

        if resp.status == 200:
            return True
        return False

    def generate_order_json(self, order, phone_number):
        products = order.split(';')
        products_info = {}
        counts = []
        products_unic = []

        for product in products:
            if product:
                products_info.update({product: products.count(product)})

        for product, product_count in products_info.items():
            products_unic.append(product)
            counts.append(product_count)

        result = {'secret': FP_TOKEN, 'product[]': products_unic, 'product_kol[]': counts, 'phone': phone_number, 'descr': "Заказ с бота ВКонтакте"}
        return result
