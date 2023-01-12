from random import randint
from typing import Callable
import click

class our_pizza:
    def __init__(self, name: str, size: str):
        if name not in ['Margherita', 'Pepperoni', 'Hawaiian']:
            raise ValueError('This pizza in not in menu!')
        if size not in ['L', 'XL']:
            raise ValueError('This size in not available!')

        self.size = size
        self.name = name

        if name == 'Margherita':
            self.name += ' 🧀'
            self.ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']

        if name == 'Pepperoni':
            self.name += ' 🍕'
            self.ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']

        if name == 'Hawaiian':
            self.name += ' 🍍'
            self.ingredients = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']

    def __str__(self):
        return f'{self.name} ({self.size})'

    def dict(self):
        """метод dict() - выводит рецепт в виде словаря"""
        recipe = {self.name: ', '.join(ingredient for ingredient in self.ingredients)}
        return recipe

    def __eq__(self, other):
        """реализуйте __eq__() для сравнения пицц
        (object.__eq__ в Python. Позволяет реализовать проверку на равенство для экземпляров пользовательских типов)"""
        if self.name == other.name and self.size == other.size:
            return True
        else:
            return False


def order(pizza: str, size: str, delivery_flag: bool):
    """Команда готовит пиццу, флаг –—delivery передает ее с курьером."""
    if delivery_flag not in [True, False]:
        raise ValueError('Delivery included, true or false')
    ordered_pizza = our_pizza(pizza, size)
    print(ordered_pizza)
    if delivery_flag == True:
        return ordered_pizza.__str__() + bake(pizza).__str__() + delivery(pizza).__str__()
    else:
        return ordered_pizza.__str__() + bake(pizza).__str__() + pickup(pizza).__str__()


def menu():
    """Команда отображает доступное меню"""
    all_pizza = [our_pizza('Margherita', 'L'), our_pizza('Pepperoni', 'L'), our_pizza('Hawaiian', 'L')]
    answer = ''
    for pizza in all_pizza:
        answer += f'- {pizza.name}: ' + ', '.join(ingredient for ingredient in pizza.ingredients) + '\n'
    return answer


def log(example: str):
    """декоратор, который выводит имя функции и время выполнения """

    def outer_wrapper(function: Callable) -> Callable:
        def inner_wrapper(*args, **kwargs):
            print(example.replace('{}', f'{randint(10, 1000)}').replace('name', function.__name__))
            function(*args, **kwargs)
        return inner_wrapper
    return outer_wrapper


"""шаблоны, в которые подставляется время"""

@log('👨‍🍳 Приготовили за {} с!')
def bake(pizza: our_pizza):
    """Готовит пиццу"""


@log('🛵 Доставили за {} с!')
def delivery(pizza: our_pizza):
    """Доставляет пиццу"""


@log('🏠 Забрали за {} с!')
def pickup(pizza: our_pizza):
    """Доставляет пиццу"""


if __name__ == '__main__':
    first_pizza = our_pizza('Pepperoni', 'XL')
    second_pizza = our_pizza('Margherita', 'L')
    print(first_pizza)
    print(first_pizza.dict())

    print(first_pizza == first_pizza)
    print(first_pizza == second_pizza)

    print(menu())
    order('Pepperoni', 'XL', delivery_flag=True)
    order('Margherita', 'L', delivery_flag=False)
