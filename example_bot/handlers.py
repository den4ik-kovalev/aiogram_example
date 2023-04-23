from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup

from .animals import Krasivosti
from .callbacks import button_weather, button_currency, button_cancel, button_endpoll
from .currency import CurrencyConverterAPI
from .dispatcher import bot, dp
from .states import CurrencyStatesGroup, PollCreationStatesGroup
from .utils import StrHelper
from .weather import WeatherAPI


@dp.message_handler(commands=["start"])
async def command_start(message: Message):
    """ Команда /start """

    # отправить приветственное сообщение
    text = "Приветствую! \n\n" \
           "/help - доступные команды" \
           "/weather - текущая погода \n" \
           "/currency - конвертер валют \n" \
           "/animals - картинка с животными \n" \
           "/poll - конструктор опросов"

    await bot.send_message(
        chat_id=message.chat.id,
        text=text
    )


@dp.message_handler(commands=["help"])
async def command_help(message: Message):
    """ Команда /help """

    # отправить сообщение со списком команд
    text = "/weather - текущая погода \n" \
           "/currency - конвертер валют \n" \
           "/animals - картинка с животными \n" \
           "/poll - конструктор опросов"

    await bot.send_message(
        chat_id=message.chat.id,
        text=text
    )


@dp.message_handler(commands=["weather"])
async def command_weather(message: Message):
    """ Команда /weather """

    # отправить сообщение с выбором города из WeatherAPI.cities
    await message.answer(
        text="Выберите город",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    button_weather(city_name)
                ]
                for city_name in WeatherAPI.cities
            ]
        )
    )


@dp.message_handler(commands=["currency"])
async def command_currency(message: Message):
    """ Команда /currency """

    # доступные пары валют для перевода в ту и другую сторону
    options = [
        ("RUB", "USD"),
        ("RUB", "EUR"),
        ("RUB", "KZT")
    ]

    # отправить сообщение со всеми доступными вариантами для конвертации
    await message.answer(
        text="Выберите валюту",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    button_currency(code_1, code_2),
                    button_currency(code_2, code_1)
                ]
            for code_1, code_2 in options
            ]
        )
    )


@dp.message_handler(state=CurrencyStatesGroup.amount)
async def text_currency_amount(message: Message, state: FSMContext):
    """ Команда /currency, после отправки сообщения с количеством """

    # получить количество валюты из сообщения
    amount = message.text

    # проверить что это валидное число
    if not StrHelper.is_positive_float(amount):
        return await message.answer("Введите корректное число")

    # получить коды валют, выбранные на предыдущем шаге
    state_data = await state.get_data()
    code_from = state_data["code_from"]
    code_to = state_data["code_to"]

    # сбросить состояние FSM
    await state.finish()

    # получить с помощью API результат конвертации
    try:
        result = CurrencyConverterAPI.convert(code_from, code_to, amount)
    except Exception:
        text = "Ошибка при обращении к сервису Exchange Rates"
    else:
        text = f"{amount} {code_from} = {result} {code_to}"

    # отправить сообщение с результатом
    await message.answer(text)


@dp.message_handler(commands=["animals"])
async def command_animals(message: Message):
    """ Команда /animals """

    # отправить сообщение со случайным фото котика
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=Krasivosti.get_cat_image()
    )


@dp.message_handler(commands=["poll"])
async def command_poll(message: Message, state: FSMContext):
    """ Команда /poll """

    # перейти к состоянию ввода заголовка опроса
    await PollCreationStatesGroup.question.set()

    # отправить ответное сообщение о прогрессе создания опроса
    message_answer = await message.answer(
        text=f"Введите заголовок опроса",
        reply_markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    button_cancel()
                ]
            ]
        )
    )

    # сохранить это сообщение внутри текущего состояния
    await state.update_data(msg=message_answer)


@dp.message_handler(state=PollCreationStatesGroup.question)
async def text_poll_question(message: Message, state: FSMContext):
    """ Команда /poll, после ввода заголовка """

    # получить заголовок из сообщения
    question = message.text

    # сохранить заголовок внутри текущего состояния
    await state.update_data(question=question, options=[])

    # перейти к состоянию выбора вариантов ответа
    await PollCreationStatesGroup.option.set()

    # удалить сообщение пользователя
    await message.delete()

    # вытащить из текущего состояния сообщение прогресса
    state_data = await state.get_data()
    msg = state_data["msg"]  # type: Message

    # обновить сообщение прогресса
    await msg.edit_text(
        text=f'Опрос: "{question}"\n'
             f'Введите первый вариант ответа',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    button_cancel()
                ]
            ]
        )
    )


@dp.message_handler(state=PollCreationStatesGroup.option)
async def text_poll_option(message: Message, state: FSMContext):
    """ Команда /poll, после ввода варианта ответа """

    # получить вариант ответа из сообщения
    option = message.text

    # сохранить вариант внутри текущего состояния
    state_data = await state.get_data()
    options = state_data["options"] + [option]
    await state.update_data(options=options)

    # вытащить из текущего состояния сообщение прогресса и обновить его
    msg = state_data["msg"]

    # сформировать сообщение с превью опроса
    lines = [f"<b>{state_data['question']}</b>"]
    for option in options:
        lines.append(f"- {option}")
    lines.append("")
    lines.append("Введите следующий вариант ответа")
    text = "\n".join(lines)

    # обновить сообщение прогресса
    await msg.edit_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    button_endpoll()
                ],
                [
                    button_cancel()
                ]
            ]
        )
    )
