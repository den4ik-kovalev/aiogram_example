__all__ = [
    "Physicist",
    "StrHelper"
]


class Physicist:
    """ Класс для работы с физическими величинами """

    @staticmethod
    def kelvin_to_celcius(k: float):
        """ Градусы Кельвина -> градусы Цельсия """
        return k - 273.15

    @staticmethod
    def hpa_to_mmhg(hpa: float):
        """ hPa -> мм.рт.ст. """
        return hpa / 1.333


class StrHelper:
    """ Класс для работы со строками """

    @classmethod
    def is_float(cls, s: str) -> bool:
        """ Проверить что строка является корректным числом """
        try:
            float(s)
            return True
        except ValueError:
            return False

    @classmethod
    def is_positive_float(cls, s: str) -> bool:
        """ Проверить что строка является положительным числом """
        return cls.is_float(s) and float(s) > 0
