import dataclasses
import requests

from .utils import Physicist


@dataclasses.dataclass
class WeatherInfo:
    """ Информация о погоде """

    description: str  # краткое описание
    temperature: float  # температура в градусах Цельсия
    pressure: int  # давление в мм.рт.ст.
    humidity: int  # влажность в %
    wind_speed: float  # скорость ветра в м/c

    def __str__(self) -> str:
        return f"{self.description.capitalize()}, {round(self.temperature)} °C\n" \
               f"Давление: {round(self.pressure)} мм.рт.ст.\n" \
               f"Влажность: {self.humidity} %\n" \
               f"Скорость ветра: {round(self.wind_speed, 2)} м/c"


class WeatherAPI:
    """ Класс для запросов к OpenWeatherMap API """

    # API key сервиса OpenWeatherMap
    APIKEY = "9e6ca428c992707c125d47356718799a"

    # название города -> id города в сервисе
    cities = {
        "Москва": 524894,
        "Санкт-Петербург": 498817,
        "Петрозаводск": 509820
    }

    @classmethod
    def weather_in_city(cls, city_id: int) -> WeatherInfo:
        """ Получить погоду в городе по id """

        # сделать GET-запрос на нужный url
        url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={cls.APIKEY}&lang=ru"
        resp = requests.get(url)
        data = resp.json()

        # вытащить результат из ответа
        return WeatherInfo(
            description=data["weather"][0]["description"],
            temperature=Physicist.kelvin_to_celcius(data["main"]["temp"]),
            pressure=Physicist.hpa_to_mmhg(data["main"]["pressure"]),
            humidity=data["main"]["humidity"],
            wind_speed=data["wind"]["speed"],
        )
