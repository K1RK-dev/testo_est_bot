from src.loader import db


class DBRequests:
    def __init__(self):
        pass

    async def db_is_user_exists(self, user_id):
        sql = 'SELECT `id` FROM `customers` WHERE `user_id`= %s' % user_id
        result = await db.request(sql)
        if result:
            return True
        return False

    async def get_customer_cart(self, user_id):
        sql = 'SELECT `cart` FROM `customers` WHERE `user_id`=%s' % user_id
        data = await db.request(sql)
        if data['cart']:
            return data['cart']
        return None

    async def get_product_info_by_article(self, article):
        sql = 'SELECT `product_name`, `product_price` FROM `product_menu` WHERE `article`=%s' % article
        result = await db.request(sql, 'fetchall')
        if result:
            return result
        return None
