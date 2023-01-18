from vkbottle.bot import Blueprint, Message
from loader import db
from keyboards.menu import main_menu_keyboard
import strings

bp = Blueprint()


@bp.on.message(text=strings.START)
async def start(message: Message):
    user_info = await bp.api.users.get(message.from_id)
    user_id = message.from_id
    firstname = user_info[0].first_name
    lastname = user_info[0].last_name
    phone_number = user_info[0].mobile_phone

    if phone_number is None:
        phone_number = 'null'

    sql_1 = 'SELECT * FROM `customers` WHERE `user_id` = %s' % user_id
    sql_2 = 'INSERT INTO `customers` (`user_id`, `firstname`, `lastname`, `phone_number`) VALUES (%s, "%s", "%s", "%s")'
    sql_2 = sql_2 % (str(user_id), str(firstname), lastname, str(phone_number))

    if await db.request(sql_1) is None:
        await db.request(sql_2)

    await message.answer(strings.HELLO % firstname, keyboard=main_menu_keyboard)
