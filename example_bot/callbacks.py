from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from .dispatcher import dp, bot
from .states import CurrencyStatesGroup, PollCreationStatesGroup
from .weather import WeatherAPI


def button_cancel() -> InlineKeyboardButton:
    """ Кнопка "Отмена" """

    return InlineKeyboardButton(
        text=f"Отмена",
        callback_data=f"cancel:"
    )


@dp.callback_query_handler(text_contains="cancel:", state="*")
async def callback_cancel(callback: CallbackQuery, state: FSMContext):
    """ Нажатие на кнопку "Отмена" """

    # сбросить текущее состояние
    await state.finish()

    # удалить сообщение, содержащее кнопку
    await callback.message.delete()


def button_weather(city_name: str) -> InlineKeyboardButton:
    """ Кнопка выбора города для информации о погоде """

    return InlineKeyboardButton(
        text=city_name,
        callback_data=f"weather:{city_name}"
    )


@dp.callback_query_handler(text_contains="weather:")
async def callback_weather(callback: CallbackQuery):
    """ Команда /weather, нажатие на кнопку выбора города """

    # получить название города
    _, city_name = callback.data.split(":")

    # получить id города для API
    city_id = WeatherAPI.cities[city_name]

    # получить с помощью API информацию о погоде
    try:
        weather_info = WeatherAPI.weather_in_city(city_id)
    except Exception:
        text = "Ошибка при обращении к сервису OpenWeatherMap"
    else:
        text = f"<b>Погода в городе {city_name}:</b>\n{weather_info}"

    # отправить сообщение с результатом
    await callback.message.answer(text)


def button_currency(code_from: str, code_to: str) -> InlineKeyboardButton:
    """ Кнопка выбора валюты для конвертирования """

    return InlineKeyboardButton(
        text=f"{code_from} -> {code_to}",
        callback_data=f"currency:{code_from}:{code_to}"
    )


@dp.callback_query_handler(text_contains="currency:")
async def callback_currency(callback: CallbackQuery, state: FSMContext):
    """ Команда /currency, нажатие на кнопку выбора валюты """

    # получить коды валют для перевода
    _, code_from, code_to = callback.data.split(":")

    # запомнить коды валют внутри состояния
    await state.update_data(code_from=code_from, code_to=code_to)

    # перейти к состоянию ввода количества денег
    await CurrencyStatesGroup.amount.set()

    # отправить ответное сообщение
    await callback.message.answer(
        text=f"Введите количество {code_from}",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    button_cancel()
                ]
            ]
        )
    )


def button_endpoll() -> InlineKeyboardButton:
    """ Кнопка завершения создания опроса """

    return InlineKeyboardButton(
        text=f"Готово",
        callback_data=f"endpoll:"
    )


@dp.callback_query_handler(text_contains="endpoll:", state=PollCreationStatesGroup.option)
async def callback_endpoll(callback: CallbackQuery, state: FSMContext):
    """ Команда /poll, нажатие на кнопку завершения создания опроса """

    # получить данные о заголовке и вариантов из текущего состояния
    state_data = await state.get_data()

    # сбросить состояние
    await state.finish()

    # вытащить из текущего состояния сообщение прогресса и обновить его
    msg = state_data["msg"]  # type: Message
    await msg.edit_text("Опрос готов, Вы можете переслать его в любой чат")

    # отправить ответное сообщение с сформированным опросом
    await bot.send_poll(
        chat_id=callback.message.chat.id,
        question=state_data["question"],
        options=state_data["options"],
        is_anonymous=False
    )
