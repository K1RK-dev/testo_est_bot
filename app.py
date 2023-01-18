import asyncio
import warnings

from vkbottle.bot import Message

from loader import bot, db
from keyboards.menu import main_menu_keyboard
from blueprints import blueprints

for bp in blueprints:
    bp.load(bot)


@bot.on.message()
async def no_understand(message: Message):
    user_info = await bp.api.users.get(message.from_id)
    user_id = message.from_id
    firstname = user_info[0].first_name
    lastname = user_info[0].last_name
    phone_number = user_info[0].mobile_phone

    if phone_number is None:
        phone_number = 'null'

    sql_1 = 'SELECT * FROM `customers` WHERE `user_id` = %s' % str(user_id)
    sql_2 = 'INSERT INTO `customers` (`user_id`, `firstname`, `lastname`, `phone_number`) VALUES (%s, "%s", "%s", "%s")'
    sql_2 = sql_2 % (str(user_id), str(firstname), lastname, str(phone_number))

    if await db.request(sql_1, 'fetchone') is None:
        await db.request(sql_2, 'fetchone')
    await message.answer('Извините, я вас не понял.\nВоспользуйтесь кнопками ниже👇', keyboard=main_menu_keyboard)


warnings.filterwarnings("ignore", category=Warning)
loop = asyncio.get_event_loop()

if __name__ == "__main__":
    print('Bot started...')
    bot.run_forever()
