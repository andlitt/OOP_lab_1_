#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Money:
    VALID_NOMINALS = [1, 2, 5, 10, 50, 100, 500, 1000, 5000]

    def __init__(self, first, second):
        if not self.check_nominal(first):
            raise ValueError(
                f"Номинал {first} не поддерживается. Допустимые:"
                f"{self.VALID_NOMINALS}"
            )
        if second < 1:
            raise ValueError(f"Количество {second} должно быть не менее 1")
        self.first = first  # номинал
        self.second = second  # количество

    # Проверка корректности номинала
    def check_nominal(self, value):
        return value in self.VALID_NOMINALS

    # Ввод с клавиатуры
    def read(self):
        try:
            first = int(input("Введите номинал купюры: "))
            second = int(input("Введите количество купюр: "))

            if not self.check_nominal(first):
                print(f"Ошибка: Номинал {first} не поддерживается")
                print(f"Допустимые номиналы: {self.VALID_NOMINALS}")
                return False

            if second < 1:
                print(f"Ошибка: Количество {second} должно быть не менее 1")
                return False

            self.first = first
            self.second = second
            return True

        except ValueError:
            print("Ошибка: Введите числовые значения")
            return False

    # Вывод на экран
    def display(self):
        print(f"Номинал: {self.first} руб.")
        print(f"Количество: {self.second} шт.")
        print(f"Общая сумма: {self.first * self.second} руб.")

    # Вычисление суммы
    def summa(self):
        return self.first * self.second


def make_money(first, second):
    try:
        # Создаем временный объект для проверки
        temp = Money(first, second)
        return temp
    except ValueError as e:
        raise ValueError(f"Ошибка создания объекта Money: {e}")
