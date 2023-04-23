from aiogram.dispatcher.filters.state import State, StatesGroup

__all__ = [
    "CurrencyStatesGroup",
    "PollCreationStatesGroup"
]


class CurrencyStatesGroup(StatesGroup):
    """ Состояния для сценария: конвертирование валюты """

    amount = State()  # ожидается ввод количества валюты


class PollCreationStatesGroup(StatesGroup):
    """ Состояния для сценария: создание опроса """

    question = State()  # ожидается ввод заголовка опроса
    option = State()  # ожидается ввод варианта ответа
