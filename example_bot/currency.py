import requests

__all__ = ["CurrencyConverterAPI"]


class CurrencyConverterAPI:
    """ Класс для запросов к Exchange Rates API """

    # API key сервиса "Exchange Rates API"
    APIKEY = "pyliI7nlHd3TlSu48KpEVXFnJy4VlfVz"

    @classmethod
    def convert(cls, code_from: str, code_to: str, amount: float) -> float:
        """ Перевести :amount валюты с кодом :code_from в валюту с кодом :code_to """

        # сделать GET-запрос на нужный url и вытащить результат из ответа
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={code_to}&from={code_from}&amount={amount}"
        resp = requests.get(url, headers={"apikey": cls.APIKEY})
        data = resp.json()
        return data["result"]
