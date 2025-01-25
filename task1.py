class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        """
        Создание и подготовка к работе объекта "Книга".

        :param name: Название книги.
        :param author: Автор книги.

        Примеры:
        >>> book = Book("Harry Potter", "J.K. Rowling")  # инициализация экземпляра класса
        >>> book.name
        'Harry Potter'
        >>> book.author
        'J.K. Rowling'
        """
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self.__name = name

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        self.__author = author

    @property
    def name(self) -> str:
        """
        Возвращает название книги.

        Инкапсуляция позволяет контролировать доступ к атрибуту __name. Мы можем добавлять логику в будущем,
        не изменяя интерфейс класса.
        """
        return self.__name

    @property
    def author(self) -> str:
        """
        Возвращает автора книги.

        Инкапсуляция позволяет контролировать доступ к атрибуту __author, обеспечивая возможность переделки логики
        без изменения интерфейса класса.
        """
        return self.__author

    def __str__(self) -> str:
        """Возвращает строковое представление книги"""
        return f"Книга: {self.name}, Автор: {self.author}"

    def __repr__(self) -> str:
        """Возвращает строку, которая представляет объект книги."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс для представления бумажной книги. """

    def __init__(self, name: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Бумажная книга".

        :param name: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц в книге.

        Примеры:
        >>> paper_book = PaperBook("Harry Potter", "J.K. Rowling", 1088) # инициализация экземпляра класса
        >>> paper_book.pages
        1088
        """
        super().__init__(name, author)  # Вызов конструктора базового класса

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.__pages = pages

    @property
    def pages(self) -> int:
        """
        Возвращает количество страниц книги.

        Инкапсуляция обеспечивает контроль доступа к атрибуту __pages, позволяя добавлять
        в будущем логику в методы без изменения интерфейса класса.
        """

        return self.__pages

    def name(self) -> str:
        """
        Переопределяет метод name и добавляет информацию о том, что это бумажная книга.

        Инкапсуляция: это позволяет расширять функциональность метода,
        не изменяя базового поведения, сохраняя при этом отсутствие прямого доступа к __name.

        Применение этого метода позволяет пользователям сразу видеть, что
        эта книга относится к категории бумажных книг.
        """
        return f"{super().name} (бумажная книга)"

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги

        Переопределен, чтобы включать количество страниц в вывод. Это полезно
        для пользователей, которые хотят быстро узнать не только название
        и автора, но и общее количество страниц в книге.
        """
        return f"{super().__str__()}, Страниц: {self.pages}"

    def __repr__(self) -> str:
        """Возвращает строку, которая представляет объект бумажной книги."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


if __name__ == "__main__":
    # Write your solution here
    import doctest
    doctest.testmod()
    pass




