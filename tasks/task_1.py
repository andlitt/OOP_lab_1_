#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from class_money import Money

if __name__ == "__main__":

    print("\nСоздание через конструктор:")
    try:
        money1 = Money(100, 5)
        money1.display()
    except ValueError as e:
        print(f"Ошибка: {e}")
