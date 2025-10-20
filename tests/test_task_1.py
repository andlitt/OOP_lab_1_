#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from tasks.class_Money import Money, make_Money


# Создание через конструктор с
def test_constructor():
    money = Money(100, 5)
    assert money.first == 100
    assert money.second == 5
    assert money.summa() == 500


# Создание через make_Money
def test_make_money():
    money = make_Money(500, 3)
    assert money.first == 500
    assert money.second == 3
    assert money.summa() == 1500


#  Попытка создания с неверным номиналом
def test_invalid_nominal():
    with pytest.raises(ValueError, match="Номинал 3 не поддерживается"):
        Money(3, 7)


# Попытка создания с отрицательным количеством
def test_invalid_quantity():
    with pytest.raises(ValueError, match="Количество -7 должно быть не менее 1"):
        Money(100, -7)


# Вычисление суммы
def test_summa_calculation():
    money = make_Money(1000, 2)
    assert money.summa() == 2000


# Тест метода check_nominal с валидными номиналами
def test_check_nominal():
    money = Money(100, 1)
    for nominal in money.VALID_NOMINALS:
        assert money.check_nominal(nominal) is True


# Тест метода check_nominal с невалидными номиналами
def test_check_nominal_invalid():
    money = Money(100, 1)
    assert money.check_nominal(3) is False
    assert money.check_nominal(25) is False
    assert money.check_nominal(200) is False
