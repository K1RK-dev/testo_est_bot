import asyncio
import warnings

from vkbottle.bot import Message
from database.db_requests import DBRequests
from src.loader import bot, db
from src.keyboards.menu import main_menu_keyboard
from src.blueprints import blueprints

for bp in blueprints:
    bp.load(bot)

db_requests = DBRequests()
@bot.on.message()
async def no_understand(message: Message):
    user_info = await bp.api.users.get(message.from_id)
    await db_requests.check_registration(user_info)

    await message.answer('Извините, я вас не понял.\nВоспользуйтесь кнопками ниже👇', keyboard=main_menu_keyboard)


warnings.filterwarnings("ignore", category=Warning)
loop = asyncio.get_event_loop()

if __name__ == "__main__":
    print('Bot started...')
    bot.run_forever()
