# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union

class Moneybox:
    def __init__(self, moneybox_volume: Union[int, float], amount_of_money: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Копилка"

        :param moneybox_volume: Объем копилки (макисмальное количество денег, которое может поместиться)
        :param amount_of_money: Количество денег в копилке

        Примеры:
        >>> moneybox = Moneybox(500, 0) # инициализация экземпляра класса
        """
        if not isinstance(moneybox_volume, (int, float)):
            raise TypeError("Объем копилки должен быть типа int или float")
        if moneybox_volume <= 0:
            raise ValueError("Объем копилки должен быть положительным числом")
        self.moneybox_volume = moneybox_volume

        if not isinstance(amount_of_money, (int, float)):
            raise TypeError("Количество денег в копилке должно быть int или float")
        if amount_of_money < 0:
            raise ValueError("Количество денег в копилке не может быть отрицательным числом")
        self.amount_of_money = amount_of_money

    def is_empty_moneybox(self) -> bool:
        """
        Функция которая проверяет является ли копилка пустой

        :return: Является ли копилка пустой

        Примеры:
        >>> moneybox = Moneybox(500, 0)
        >>> moneybox.is_empty_moneybox()
        """
        ...

    def add_money_to_moneybox(self, money:  Union[int, float]) -> None:
        """
        Добавление денег в копилку
        :param money: Количество добавляемых денег

        :raise ValueError: Если количество добавляемых денег превышает свободное место в копилке, то вызываем ошибку

        Примеры:
        >>> moneybox = Moneybox(500, 0)
        >>> moneybox.add_money_to_moneybox(200)
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Количество добавляемых денег должно быть типа int или float")
        if money < 0:
            raise ValueError("Количество добавляемых денег должно быть положительным числом")
        if money > self.moneybox_volume-self.amount_of_money:
            raise ValueError("Количество добавляемых денег должно быть не больше свободного места в копилке")
        ...



class Vector:
    def __init__(self, x: Union[int, float], y: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Вектор"

        :param x: Координата x
        :param y: Координата y

        Примеры:
        >>> vector = Vector(2.5, 6) # инициализация экземпляра класса
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Координата x должна быть типа int или float")
        self.x = x

        if not isinstance(y, (int, float)):
            raise TypeError("Координата y должна быть типа int или float")
        self.y = y

    def vector_len(self) -> float:
        """
        Функция, которая возвращает длину вектора

        :return: Длина вектора

        Примеры:
        >>> vector = Vector(2.5, 6)
        >>> len_vector = vector.vector_len()
        """
        ...

    def mult_by_num(self, num: Union[int, float]) -> None:
        """
        Функция, которая умножает вектор на число

        :param num: Число, на которое необходимо умножить вектор

        Примеры:
        >>> vector = Vector(2.5, 6) # инициализация экземпляра класса
        >>> vector.mult_by_num(6)
        """
        if not isinstance(num, (int, float)):
            raise TypeError("Координата x должна быть типа int или float")
        ...

class Book:
    def __init__(self, name: str, num_pages: int, rating: float):
        """
        Создание и подготовка к работе объекта "Книга"

        :param name: Название книги
        :param num_pages: Количество страниц в книге
        :param rating: Рейтинг книги

        Примеры:
        >>> book = Book("Harry Potter", 1000, 6.4) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название книги  должно быть типа str")
        self.name = name
        if not isinstance(num_pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if num_pages < 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.num_pages = num_pages
        if not isinstance(rating,float):
            raise TypeError("Рейтинг должен быть типа float")
        if rating < 0 or rating > 10:
            raise ValueError("Рейтинг должен быть в диапазоне от 0 до 10")
        self.rating = rating

    def if_more_book_rate(self, rate_for_comp: float) -> bool:
        """
        Функция, которая сравнивает рейтинг книги с переданным в функцию

        :param rate_for_comp: Рейтинг для сравнения

        :return: Является ли рейтинг книги больше рейтинга для сравнения

        Примеры:
        >>> book = Book("Harry Potter", 1000, 6.4)
        >>> res = book.if_more_book_rate(8.5)
        """
        if not isinstance(rate_for_comp, float):
            raise TypeError("Рейтинг должен быть типа float")
        ...

    def change_rating(self, new_rating: float) -> None:
        """
        Функция, которая изменяет рейтинг книгя

        :param new_rating: Новый рейтинг книги

        Примеры:
        >>> book = Book("Harry Potter", 1000, 6.4)
        >>> book.change_rating(8.9)
        """
        if not isinstance(new_rating,float):
            raise TypeError("Рейтинг должен быть типа float")
        if new_rating < 0 or new_rating > 10:
            raise ValueError("Рейтинг должен быть в диапазоне от 0 до 10")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
