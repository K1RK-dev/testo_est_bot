import json
from vkbottle import TemplateElement, Keyboard, Text, KeyboardButtonColor
from src.loader import db


async def generate_carousels():
    sql = 'SELECT `product_name`, `product_price`, `ingredients`, `photo_id`, `article` from `product_menu`'
    sql_result = await db.request(sql, 'fetchall')

    carousels, templates, keyboards = [], [], []
    items_count, keyboard_index = 0, -1

    if not sql_result is None:
        for menu_item in sql_result:
            if items_count == 10:
                carousel = json.dumps({"type": "carousel", "elements": templates}, ensure_ascii=False).encode('utf-8').decode()
                carousels.append(carousel)
                items_count = 0
                templates = []

            kb = (Keyboard(one_time=False, inline=True)
                  .add(Text('Добавить в корзину', payload={'add_to_cart': menu_item['article']}), color=KeyboardButtonColor.POSITIVE)
                  .add(Text('Состав', payload={'get_ingredients': menu_item['article']}), color=KeyboardButtonColor.POSITIVE))
            keyboards.append(kb)
            keyboard_index += 1

            te = TemplateElement(title=menu_item['product_name'],
                                 photo_id=menu_item['photo_id'],
                                 description='⠀',
                                 buttons=keyboards[keyboard_index].get_json())
            items_count += 1
            templates.append(te.raw)
    return carousels
