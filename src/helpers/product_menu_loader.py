import json
from vkbottle import TemplateElement, Keyboard, Text, KeyboardButtonColor
from database.db_requests import DBRequests

db_requests = DBRequests()


async def generate_carousels():
    product_menu = await db_requests.get_product_menu()
    if product_menu is None:
        return None

    carousels, templates, keyboards = [], [], []
    items_count, keyboard_index = 0, -1

    for menu_item in product_menu:

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

        if items_count == 10 or items_count == len(product_menu):
            carousel = json.dumps({"type": "carousel", "elements": templates}, ensure_ascii=False).encode('utf-8').decode()
            carousels.append(carousel)
            items_count = 1
            templates = []

    return carousels
