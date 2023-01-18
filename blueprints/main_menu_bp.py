from vkbottle.bot import Blueprint, Message
from keyboards.menu import operator_chat_keyboard, cart_keyboard
from product_menu_loader import generate_carousels
import strings

bp = Blueprint()


@bp.on.message(text=strings.PRODUCT_MENU_BTN, payload={"main_menu": "show_product_menu"})
async def show_product_menu(message: Message):
    carousels = await generate_carousels()
    count = 0
    for carousel in carousels:
        count += 1
        await bp.api.messages.send(peer_id=message.from_id, message='Меню: Часть ' + str(count), template=carousel, random_id=0)


@bp.on.message(text=strings.OPERATOR_COMMUNICATION_BTN, payload={'main_menu': 'chat_with_operator'})
async def open_operator_chat(message: Message):
    await message.answer(strings.OPERATOR_COMMUNICATION_MENU, keyboard=operator_chat_keyboard)


@bp.on.message(text=strings.CART_BTN, payload={"main_menu": "cart"})
async def open_cart(message: Message):
    await message.answer(strings.CART_MENU, keyboard=cart_keyboard)
