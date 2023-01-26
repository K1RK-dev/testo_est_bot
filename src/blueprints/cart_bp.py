from vkbottle.bot import Blueprint, Message
from src.keyboards.menu import main_menu_keyboard, cart_keyboard, product_size_keyboard
from src.states.states import SendOrder, AddToCart
from ast import literal_eval
from API.frontpad_api import FrontPadAPI
from database.db_requests import DBRequests
from src.helpers.message_generator import MessageGenerator
from src.helpers.validator import validate_phone_number
import src.helpers.strings as strings

bp = Blueprint()
db_requests = DBRequests()
msg_generator = MessageGenerator()


@bp.on.message(text=strings.CART_CONTENTS_BTN, payload={'cart_menu': 'show_cart'})
async def show_cart(message: Message):
    user_id = message.from_id
    user_info = await bp.api.users.get(user_id)
    await db_requests.check_registration(user_info)

    if not message.payload:
        await message.answer(strings.DONT_UNDERSTAND)

    else:
        customer_cart = await db_requests.get_customer_cart(user_id)
        if customer_cart is None:
            await message.answer(strings.CART_IS_EMPTY, keyboard=cart_keyboard)

        else:
            articles = list(filter(None, customer_cart.split(';')))
            names, prices, sizes = [], [], []

            for article in articles:
                product = await db_requests.get_product_by_article(article)
                if product:
                    names.append(product['product_name'])
                    prices.append(product['product_price'])
                    sizes.append(product['size'])

            answer = msg_generator.generate_cart_contents_message(names, prices, sizes)
            await message.answer(answer, keyboard=cart_keyboard)


@bp.on.message(text=strings.SEND_ORDER_BTN, payload={'cart_menu': 'send_order'})
async def send_order(message: Message):
    user_id = message.from_id
    user_info = await bp.api.users.get(user_id)

    await db_requests.check_registration(user_info)

    is_cart = await db_requests.get_customer_cart(user_id)
    if not is_cart:
        await message.answer(strings.CART_IS_EMPTY)

    else:
        await message.answer(strings.GET_PHONE_NUMBER)
        await bp.state_dispenser.set(user_id, SendOrder.PHONE_NUMBER)


@bp.on.message(state=SendOrder.PHONE_NUMBER, text='<phone_number>')
async def send_order(message: Message, phone_number=None):
    user_id = message.from_id
    user_info = await bp.api.users.get(user_id)
    await db_requests.check_registration(user_info)

    is_phone_number_valid = validate_phone_number(str(phone_number))
    if not is_phone_number_valid:
        if message.payload:
            await message.answer(strings.CANCEL_ORDER)
        else:
            await message.answer(strings.INCORRECT_PHONE_NUMBER)

    else:
        await db_requests.update_customer_phone_number(user_id, phone_number)
        order = await db_requests.get_customer_cart(user_id)
        if order:
            order_price = await db_requests.get_customer_cart_price(user_id)
            await db_requests.create_order(str(message.from_id), order, order_price, str(phone_number))
            # SENDING REQUEST
            fp = FrontPadAPI()
            order_json = fp.generate_order_json(order, phone_number)
            is_send = fp.send_order(order_json)
            if is_send:
                await message.answer(strings.ORDER_CREATED)
                await db_requests.clear_customer_cart(user_id)
            else:
                await message.answer(strings.CREATE_ORDER_ERROR)
        else:
            await message.answer(strings.CART_IS_EMPTY)

    await bp.state_dispenser.delete(message.peer_id)


@bp.on.message(text=strings.CLEAR_CART_BTN, payload={'cart_menu': 'clear_cart'})
async def clear_cart(message: Message):
    user_id = message.from_id
    user_info = await bp.api.users.get(user_id)
    await db_requests.check_registration(user_info)

    await db_requests.clear_customer_cart(message.from_id)
    await message.answer(strings.CART_CLEARED, keyboard=cart_keyboard)


@bp.on.message(text=strings.BACK_BTN, payload={'cart_menu': 'back'})
async def back(message: Message):
    user_info = await bp.api.users.get(message.from_id)
    await db_requests.check_registration(user_info)

    await message.answer(strings.MAIN_MENU, keyboard=main_menu_keyboard)


@bp.on.message(text=strings.ADD_TO_CART_BTN)
async def add_to_cart(message: Message):
    user_id = message.from_id
    user_info = await bp.api.users.get(user_id)
    await db_requests.check_registration(user_info)

    if not message.payload:
        await message.answer(strings.DONT_UNDERSTAND, keyboard=main_menu_keyboard)

    else:
        article = literal_eval(message.payload)["add_to_cart"]

        await message.answer(strings.CHOOSE_SIZE, keyboard=product_size_keyboard)
        await bp.state_dispenser.set(user_id, AddToCart.CHOOSE_SIZE, payload={'cart': article})


@bp.on.message(state=AddToCart.CHOOSE_SIZE, text='<size>')
async def add_to_cart(message: Message, size=None):
    if not size:
        await message.answer(strings.DONT_UNDERSTAND, keyboard=main_menu_keyboard)
        await bp.state_dispenser.delete(message.from_id)
    else:
        if size != '33см' and size != '40см':
            await message.answer(strings.DONT_UNDERSTAND, keyboard=main_menu_keyboard)
            await bp.state_dispenser.delete(message.from_id)
        else:
            user_info = await bp.api.users.get(message.from_id)
            await db_requests.check_registration(user_info)

            user_id = message.from_id
            state = await bp.state_dispenser.get(message.from_id)
            article = state.payload['payload']['cart']
            size = literal_eval(message.payload)['product']
            if size == 'big':
                article = int(article) + 1
                article = str(article)
                while len(article) != 5:
                    article = '0' + article

            product = await db_requests.get_product_by_article(article)
            previous_cart = await db_requests.get_customer_cart(user_id)
            previous_cart_price = await db_requests.get_customer_cart_price(user_id)
            #
            if previous_cart and previous_cart_price:
                new_cart = previous_cart + article + ';'
                new_cart_price = str(int(previous_cart_price) + int(product['product_price']))
            else:
                new_cart = article + ';'
                new_cart_price = product['product_price']
            await db_requests.update_customer_cart(user_id, new_cart, new_cart_price)

            if size == 'big':
                size = '40см'
            else:
                size = '33см'

            await message.answer(msg_generator.generate_product_added_message(product['product_name'], size), keyboard=main_menu_keyboard)
            await bp.state_dispenser.delete(message.peer_id)


@bp.on.message(text=strings.GET_COMPOSITION_BTN)
async def get_ingredients(message: Message):
    user_info = await bp.api.users.get(message.from_id)
    await db_requests.check_registration(user_info)

    if not message.payload:
        await message.answer(strings.DONT_UNDERSTAND, keyboard=main_menu_keyboard)

    else:
        article = literal_eval(message.payload)['get_ingredients']
        product = await db_requests.get_product_by_article(article)
        if product:
            answer = msg_generator.generate_product_composition_message(product['product_name'], product['ingredients'])
            await message.answer(answer)
