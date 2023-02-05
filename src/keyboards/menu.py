from vkbottle.tools import Keyboard, KeyboardButtonColor, Text
import src.helpers.strings as strings

main_menu_keyboard = (
    Keyboard(one_time=False, inline=False)
    .add(Text(strings.PRODUCT_MENU_BTN, payload={'main_menu': 'show_product_menu'}), color=KeyboardButtonColor.POSITIVE)
    .add(Text(strings.OPERATOR_COMMUNICATION_BTN, payload={'main_menu': 'chat_with_operator'}), color=KeyboardButtonColor.POSITIVE)
    .row()
    .add(Text(strings.CART_BTN, payload={'main_menu': 'cart'}), color=KeyboardButtonColor.POSITIVE)
)

operator_chat_keyboard = (
    Keyboard(one_time=False, inline=False)
    .add(Text(strings.START_OPERATOR_CHAT_BTN, payload={'operator_chat_menu': 'open_operator_chat'}), color=KeyboardButtonColor.POSITIVE)
    .add(Text(strings.GET_OPERATOR_PHONE_BTN, payload={'operator_chat_menu': 'get_phone_number'}), color=KeyboardButtonColor.POSITIVE)
    .row()
    .add(Text(strings.BACK_BTN, payload={'operator_chat_menu': 'back'}), color=KeyboardButtonColor.NEGATIVE)
)

cart_keyboard = (
    Keyboard(one_time=False, inline=False)
    .add(Text(strings.CART_CONTENTS_BTN, payload={'cart_menu': 'show_cart'}), color=KeyboardButtonColor.POSITIVE)
    .add(Text(strings.SEND_ORDER_BTN, payload={'cart_menu': 'send_order'}), color=KeyboardButtonColor.POSITIVE)
    .row()

    .add(Text(strings.CLEAR_CART_BTN, payload={'cart_menu': 'clear_cart'}), color=KeyboardButtonColor.NEGATIVE)
    .row()
    .add(Text(strings.BACK_BTN, payload={'cart_menu': 'back'}), color=KeyboardButtonColor.NEGATIVE)
)

product_size_keyboard = (
    Keyboard(one_time=True, inline=False)
    .add(Text(strings.PIZZA_SIZE_SMALL, payload={'product': 'small'}), color=KeyboardButtonColor.POSITIVE)
    .add(Text(strings.PIZZA_SIZE_BIG, payload={'product': 'big'}), color=KeyboardButtonColor.POSITIVE)
)

carousel_keyboard = (
    Keyboard(one_time=False, inline=False)
    .add(Text(strings.ADD_TO_CART_BTN, payload={'carousel': 'add_to_cart'}), color=KeyboardButtonColor.POSITIVE)
    .add(Text(strings.GET_COMPOSITION_BTN, payload={'carousel': 'get_ingredients'}), color=KeyboardButtonColor.POSITIVE)
)

order_type_keyboard = (
    Keyboard(one_time=True, inline=False)
    .add(Text(strings.ORDER_TYPE_DELIVERY, payload={'order_type': 'delivery'}), color=KeyboardButtonColor.POSITIVE)
    .add(Text(strings.ORDER_TYPE_PICKUP, payload={'order_type': 'pickup'}), color=KeyboardButtonColor.POSITIVE)
)