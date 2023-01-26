from src.helpers.strings import SOMETHING_WRONG


class MessageGenerator:
    def __init__(self):
        pass

    def generate_cart_contents_message(self, names, prices, sizes):
        result = ''
        cart_price = 0
        for i in range(0, len(names)):
            result += str(i + 1) + ')' + names[i] + '(' + sizes[i] + 'см)' + ': ' + prices[i] + 'руб.\n'
            cart_price += int(prices[i])
        result += 'Сумма: ' + str(cart_price) + 'руб.'

        return result

    def generate_product_composition_message(self, product_name, ingredients):
        ingredient_index = 0
        ingredients_list = ingredients.split(',')
        result = 'Состав товара "' + product_name + '":'
        for ingredient in ingredients_list:
            ingredient_index += 1
            result += '\n' + str(ingredient_index) + ')' + ingredient
        return result

    def generate_product_added_message(self, name, size):
        if name:
            return 'Товар: ' + '"' + name + '(' + size + ')' + '" добавлен в корзину.'
        return SOMETHING_WRONG
