from vkbottle import BaseStateGroup

class SendOrder(BaseStateGroup):
    START = 0
    PHONE_NUMBER = 1

class AddToCart(BaseStateGroup):
    START = 0
    CHOOSE_SIZE = 1
