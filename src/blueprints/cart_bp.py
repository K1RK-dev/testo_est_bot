from vkbottle.bot import Blueprint, Message
from src.keyboards.menu import main_menu_keyboard, cart_keyboard
from src.states.states import SendOrder
from src.loader import db
from ast import literal_eval
from datetime import datetime
from API.frontpad_api import FrontPadAPI
from database.db_requests import DBRequests
from src.helpers.message_generator import MessageGenerator
import src.helpers.strings as strings

bp = Blueprint()
db_requests = DBRequests()
msg_generator = MessageGenerator()

@bp.on.message(text=strings.CART_CONTENTS_BTN, payload={'cart_menu': 'show_cart'})
async def show_cart(message: Message):
    user_id = message.from_id

    if not db_requests.db_is_user_exists(user_id):
        await message.answer(strings.USER_NOT_REGISTERED)
    else:

        customer_cart = await db_requests.get_customer_cart(user_id)
        if customer_cart is None:
            await message.answer(strings.CART_IS_EMPTY, keyboard=cart_keyboard)

        else:
            articles = customer_cart.split(';')[:-1]
            names = []
            prices = []

            for article in articles:
                product_info = await db_requests.get_product_info_by_article(article)
                if product_info:
                    for value in product_info:
                        name, price = value['product_name'], value['product_price']
                        names.append(name)
                        prices.append(price)

                    answer = msg_generator.generate_cart_contents_message(names, prices)
                    await message.answer(answer, keyboard=cart_keyboard)


@bp.on.message(text=strings.SEND_ORDER_BTN, payload={'cart_menu': 'send_order'})
async def send_order(message: Message):
    if not db_requests.db_is_user_exists(message.from_id):
        await message.answer(strings.USER_NOT_REGISTERED)
    else:
        await message.answer(strings.GET_PHONE_NUMBER)
        await bp.state_dispenser.set(message.peer_id, SendOrder.PHONE_NUMBER)


@bp.on.message(state=SendOrder.PHONE_NUMBER, text='<phone_number>')
async def send_order(message: Message, phone_number=None):
    if phone_number:
        if len(str(phone_number)) <= 20:
            order_sql = 'SELECT `cart` FROM `customers` WHERE user_id=%s' % message.from_id
            order_price_sql = 'SELECT `cart_price` FROM `customers` WHERE user_id=%s' % message.from_id
            update_phone_sql = 'UPDATE `customers` SET `phone_number`=%s WHERE user_id=%s' % (str(phone_number), message.from_id)
            clear_cart_sql = 'UPDATE `customers` SET `cart`=%s, `cart_price`=%s WHERE user_id=%s' % ('Null', '0', message.from_id)

            await db.request(update_phone_sql)
            order = await db.request(order_sql)
            if order['cart']:
                order_price = await db.request(order_price_sql)
                now = datetime.now()
                dt_string = now.strftime("%d.%m.%Y %H:%M:%S")
                create_order_sql = 'INSERT INTO `orders` (`user_id`, `order`, `order_price`, `phone_number`, `order_dt`) VALUES (%s, "%s", %s, %s, "%s")' % (str(message.from_id),
                                                                                                                                                             order['cart'],
                                                                                                                                                             order_price['cart_price'],
                                                                                                                                                             str(phone_number),
                                                                                                                                                             dt_string)
                await db.request(create_order_sql)
                #sending
                fp = FrontPadAPI()
                order_json = fp.generate_order_json(order['cart'])
                is_send = fp.send_order(order_json)
                if is_send:
                    await message.answer(strings.ORDER_CREATED)
                    await db.request(clear_cart_sql)
                else:
                    await message.answer(strings.CREATE_ORDER_ERROR)
            else:
                await message.answer(strings.CART_IS_EMPTY)
        else:
            await message.answer(strings.INCORRECT_PHONE_NUMBER)
    else:
        await message.answer(strings.INCORRECT_PHONE_NUMBER)

    await bp.state_dispenser.delete(message.peer_id)


@bp.on.message(text=strings.CLEAR_CART_BTN, payload={'cart_menu': 'clear_cart'})
async def clear_cart(message: Message):
    if not db_requests.db_is_user_exists(message.from_id):
        await message.answer(strings.USER_NOT_REGISTERED)
    else:
        clear_cart_sql = 'UPDATE `customers` SET `cart`=NULL WHERE user_id=%s' % message.from_id
        clear_cart_price_sql = 'UPDATE `customers` SET `cart_price`=NULL WHERE user_id=%s' % message.from_id
        await db.request(clear_cart_sql)
        await db.request(clear_cart_price_sql)
        await message.answer(strings.CART_CLEARED, keyboard=cart_keyboard)


@bp.on.message(text=strings.BACK_BTN, payload={'cart_menu': 'back'})
async def back(message: Message):
    await message.answer(strings.GO_BACK, keyboard=main_menu_keyboard)


@bp.on.message(text=strings.ADD_TO_CART_BTN)
async def add_to_cart(message: Message):
    if not db_requests.db_is_user_exists(message.from_id):
        await message.answer(strings.USER_NOT_REGISTERED)
    else:
        if message.payload:
            payload_code = literal_eval(message.payload)["add_to_cart"]
            user_id = message.from_id
            product_name = await db.request('SELECT `product_name` FROM `product_menu` WHERE `article`=%s' % payload_code)
            product_price = await db.request(
                'SELECT `product_price` FROM `product_menu` WHERE `article`=%s' % payload_code)

            previous_cart = await db.request('SELECT `cart` FROM `customers` WHERE user_id=%s' % user_id)
            previous_cart_price = await db.request('SELECT `cart_price` FROM `customers` WHERE user_id=%s' % user_id)
            if previous_cart['cart'] is None:
                new_cart = payload_code + ';'
                new_cart_price = product_price['product_price']
            else:
                if previous_cart_price['cart_price'] is None:
                    previous_cart_price['cart_price'] = 0

                new_cart = previous_cart['cart'] + payload_code + ';'
                new_cart_price = str(int(previous_cart_price['cart_price']) + int(product_price['product_price']))

            update_cart_sql = 'UPDATE `customers` SET `cart`="%s" WHERE user_id=%s' % (new_cart, user_id)
            update_cart_price_sql = 'UPDATE `customers` SET `cart_price`=%s WHERE user_id=%s' % (
                new_cart_price, user_id)

            await db.request(update_cart_sql)
            await db.request(update_cart_price_sql)
            await message.answer('Товар: ' + '"' + product_name['product_name'] + '" добавлен в корзину.')

        else:
            await message.answer(strings.DONT_UNDERSTAND, keyboard=main_menu_keyboard)


@bp.on.message(text=strings.GET_COMPOSITION_BTN)
async def get_ingredients(message: Message):
    if not db_requests.db_is_user_exists(message.from_id):
        await message.answer(strings.USER_NOT_REGISTERED, keyboard=main_menu_keyboard)
    elif not message.payload:
        await message.answer(strings.DONT_UNDERSTAND, keyboard=main_menu_keyboard)

    else:
        payload_code = literal_eval(message.payload)['get_ingredients']
        product_name = await db.request('SELECT `product_name` FROM `product_menu` WHERE `article`=%s' % payload_code)
        ingredients = await db.request('SELECT `ingredients` FROM `product_menu` WHERE `article`=%s' % payload_code)

        if ingredients:
            answer = msg_generator.generate_product_composition_message(product_name, ingredients)
            await message.answer(answer)
