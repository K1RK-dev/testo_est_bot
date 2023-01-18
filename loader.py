from vkbottle.bot import Bot
from vkbottle import CtxStorage

import config
from database import connector

bot = Bot(token=config.TOKEN)
ctx = CtxStorage()
db = connector.DataBase(
    host=config.HOST,
    user=config.DB_USER,
    db=config.DB_NAME,
    password=config.DB_PASSWORD,
    port=3306
)
