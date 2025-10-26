#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from triangle_package import Triangle

if __name__ == "__main__":

    # Неверно заданы углы
    print("\n1. Создание через конструктор:")
    try:
        triangle1 = Triangle(3, 3, 4, 60, 60, 61)
    except ValueError as e:
        print(f"Ошибка: {e} \n")

    # Неверно заданы стороны
    try:
        triangle2 = Triangle(3, 3, 6, 60, 60, 60)
    except ValueError as e:
        print(f"Ошибка: {e} \n")

    print("\n2. Изменение полей через read:")
    triangle3 = Triangle(4, 4, 4, 60, 60, 60)
    triangle3.display()

    if triangle3.read():
        triangle3.display()
