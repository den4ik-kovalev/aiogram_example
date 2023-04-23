import random

__all__ = ["Krasivosti"]


class Krasivosti:
    """ Класс для работы с изображениями животных """

    # список url картинок с котиками
    cats = [
        'https://krasivosti.pro/uploads/posts/2021-04/1617773425_15-p-koshka-oboi-samie-milie-kotiki-15.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773435_27-p-koshka-oboi-samie-milie-kotiki-31.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773428_47-p-koshka-oboi-samie-milie-kotiki-53.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773401_20-p-koshka-oboi-samie-milie-kotiki-22.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773459_38-p-koshka-oboi-samie-milie-kotiki-42.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773448_5-p-koshka-oboi-samie-milie-kotiki-5.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773484_43-p-koshka-oboi-samie-milie-kotiki-49.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773478_50-p-koshka-oboi-samie-milie-kotiki-56.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773489_31-p-koshka-oboi-samie-milie-kotiki-35.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773425_14-p-koshka-oboi-samie-milie-kotiki-14.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773481_44-p-koshka-oboi-samie-milie-kotiki-50.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773398_40-p-koshka-oboi-samie-milie-kotiki-44.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773472_52-p-koshka-oboi-samie-milie-kotiki-58.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773405_22-p-koshka-oboi-samie-milie-kotiki-24.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773458_46-p-koshka-oboi-samie-milie-kotiki-52.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773464_16-p-koshka-oboi-samie-milie-kotiki-16.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773423_21-p-koshka-oboi-samie-milie-kotiki-23.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773387_2-p-koshka-oboi-samie-milie-kotiki-2.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773435_29-p-koshka-oboi-samie-milie-kotiki-33.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773412_26-p-koshka-oboi-samie-milie-kotiki-30.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773407_37-p-koshka-oboi-samie-milie-kotiki-41.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773434_24-p-koshka-oboi-samie-milie-kotiki-27.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773393_12-p-koshka-oboi-samie-milie-kotiki-12.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773437_35-p-koshka-oboi-samie-milie-kotiki-39.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773459_19-p-koshka-oboi-samie-milie-kotiki-21.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773437_1-p-koshka-oboi-samie-milie-kotiki-1.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773490_49-p-koshka-oboi-samie-milie-kotiki-55.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773414_28-p-koshka-oboi-samie-milie-kotiki-32.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773472_36-p-koshka-oboi-samie-milie-kotiki-40.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773400_25-p-koshka-oboi-samie-milie-kotiki-28.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773431_33-p-koshka-oboi-samie-milie-kotiki-37.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773467_3-p-koshka-oboi-samie-milie-kotiki-3.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773464_51-p-koshka-oboi-samie-milie-kotiki-57.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773461_41-p-koshka-oboi-samie-milie-kotiki-45.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773425_30-p-koshka-oboi-samie-milie-kotiki-34.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773400_6-p-koshka-oboi-samie-milie-kotiki-6.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773422_8-p-koshka-oboi-samie-milie-kotiki-8.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773417_11-p-koshka-oboi-samie-milie-kotiki-11.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773455_48-p-koshka-oboi-samie-milie-kotiki-54.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773494_42-p-koshka-oboi-samie-milie-kotiki-48.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773465_10-p-koshka-oboi-samie-milie-kotiki-10.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773451_18-p-koshka-oboi-samie-milie-kotiki-20.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773450_7-p-koshka-oboi-samie-milie-kotiki-7.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773458_32-p-koshka-oboi-samie-milie-kotiki-36.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773454_34-p-koshka-oboi-samie-milie-kotiki-38.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773417_4-p-koshka-oboi-samie-milie-kotiki-4.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773401_23-p-koshka-oboi-samie-milie-kotiki-26.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773493_39-p-koshka-oboi-samie-milie-kotiki-43.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773458_53-p-koshka-oboi-samie-milie-kotiki-60.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773397_13-p-koshka-oboi-samie-milie-kotiki-13.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773466_45-p-koshka-oboi-samie-milie-kotiki-51.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773463_17-p-koshka-oboi-samie-milie-kotiki-17.jpg',
        'https://krasivosti.pro/uploads/posts/2021-04/1617773396_9-p-koshka-oboi-samie-milie-kotiki-9.jpg'
    ]

    @classmethod
    def get_cat_image(cls):
        """ Получить случайный url картинки с котиком """
        return random.choice(cls.cats)
