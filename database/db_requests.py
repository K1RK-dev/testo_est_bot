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

    async def check_registration(self, user_info):
        user_id = user_info[0].id
        firstname = user_info[0].first_name
        lastname = user_info[0].last_name
        phone_number = user_info[0].mobile_phone

        if phone_number is None:
            phone_number = 'null'

        sql_2 = 'INSERT INTO `customers` (`user_id`, `firstname`, `lastname`, `phone_number`, `cart_price`) VALUES (%s, "%s", "%s", "%s", "%s")'
        sql_2 = sql_2 % (str(user_id), str(firstname), lastname, str(phone_number), "0")

        is_registred = await self.db_is_user_exists(user_id)
        if not is_registred:
            await db.request(sql_2)

    async def get_customer_cart(self, user_id):
        sql = 'SELECT `cart` FROM `customers` WHERE `user_id`=%s' % user_id
        result = await db.request(sql)
        if result:
            return result['cart']
        return None

    async def clear_customer_cart(self, user_id):
        sql = 'UPDATE `customers` SET `cart`=%s, `cart_price`=%s WHERE user_id=%s' % ('Null', '0', user_id)
        try:
            await db.request(sql)
            return True
        except Exception as e:
            print(str(e))
            return False

    async def get_customer_cart_price(self, user_id):
        sql = 'SELECT `cart_price` FROM `customers` WHERE user_id=%s' % user_id
        result = await db.request(sql)
        if result:
            return result['cart_price']
        return None

    async def update_customer_phone_number(self, user_id, phone_number):
        sql = 'UPDATE `customers` SET `phone_number`=%s WHERE user_id=%s' % (phone_number, user_id)
        try:
            await db.request(sql)
            return True
        except Exception as e:
            print(str(e))
            return False

    async def update_customer_cart(self, user_id, cart, price):
        sql = 'UPDATE `customers` SET `cart`="%s", `cart_price`=%s WHERE user_id=%s' % (cart, price, user_id)
        try:
            await db.request(sql)
            return True
        except Exception as e:
            print(str(e))
            return False

    async def create_order(self, user_id, order, price, phone_number):
        from datetime import datetime
        now = datetime.now()
        dt_string = now.strftime("%d.%m.%Y %H:%M:%S")
        sql = 'INSERT INTO `orders` (`user_id`, `order`, `order_price`, `phone_number`, `order_dt`) VALUES (%s, "%s", %s, %s, "%s")' % (
        user_id, order, price, phone_number, dt_string)
        try:
            await db.request(sql)
            return True
        except Exception as e:
            print(str(e))
            return False

    async def get_product_by_article(self, article):
        sql = 'SELECT `product_name`, `product_price`, `ingredients`, `size` FROM `product_menu` WHERE `article`=%s' % article
        try:
            result = await db.request(sql)
            return result
        except Exception as e:
            print(str(e))
            return None

    async def get_product_menu(self):
        sql = 'SELECT `product_name`, `product_price`, `ingredients`, `article`, `photo_id` from `product_menu` WHERE `size`=33'
        try:
            result = await db.request(sql, 'fetchall')
            return result
        except Exception as e:
            print(str(e))
            return None