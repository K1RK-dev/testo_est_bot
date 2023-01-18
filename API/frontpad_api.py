import requests
from config import FP_TOKEN


class FrontPadAPI:
    def __init__(self):
        pass

    def send_order(self, data):
        data.update({"secret": FP_TOKEN})
        print(data)
        response = requests.post('https://app.frontpad.ru/api/index.php?new_order', data)
        print(response.json())
        if response.json()['result'] == 'success':
            return True
        return False

    def generate_order_json(self, order):
        products = order.split(';')
        products_info = {}
        counts = []
        products_unic = []

        for product in products:
            if product:
                products_info.update({product: products.count(product)})

        for product in products_info.keys():
            products_unic.append(product)
        for product_count in products_info.values():
            counts.append(product_count)

        result = {'product': products_unic, 'product_kol': counts}
        return result
