from vkbottle.bot import Blueprint, Message
from database.db_requests import DBRequests
from src.keyboards.menu import main_menu_keyboard
import src.helpers.strings as strings

bp = Blueprint()
db = DBRequests()


@bp.on.message(text=strings.START)
async def start(message: Message):
    user_info = await bp.api.users.get(message.from_id)
    firstname = user_info[0].first_name
    await db.check_registration(user_info)
    await message.answer(strings.HELLO % firstname, keyboard=main_menu_keyboard)