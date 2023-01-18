from vkbottle.bot import Blueprint, Message

import src.helpers.strings as strings
from src.keyboards.menu import main_menu_keyboard

bp = Blueprint()


@bp.on.message(text=strings.START_OPERATOR_CHAT_BTN, payload={'operator_chat_menu': 'open_operator_chat'})
async def open_operator_chat(message: Message):
    await message.answer(strings.OPERATOR_PROFILE)


@bp.on.message(text=strings.GET_OPERATOR_PHONE_BTN, payload={'operator_chat_menu': 'get_phone_number'})
async def get_phone_number(message: Message):
    await message.answer(strings.OPERATOR_PHONE)


@bp.on.message(text=strings.BACK_BTN, payload={'operator_chat_menu': 'back'})
async def back(message: Message):
    await message.answer(strings.GO_BACK, keyboard=main_menu_keyboard)
