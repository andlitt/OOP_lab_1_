#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from tasks.class_Triangle import Triangle


# Создание через конструктор с валидными данными
def test_constructor_valid():
    triangle = Triangle(3, 4, 5, 90, 53.13, 36.87)
    assert triangle.a == 3
    assert triangle.b == 4
    assert triangle.c == 5
    assert triangle.alpha == 90
    assert triangle.beta == 53.13
    assert triangle.gamma == 36.87


# Неверно заданы стороны
def test_invalid_sides():
    with pytest.raises(
        ValueError,
        match="Треугольник существует, когда сумма"
        " длин любых двух его сторон больше длины третьей стороны",
    ):
        Triangle(3, 3, 6, 60, 60, 60)


# Неверно заданы углы
def test_invalid_angles():
    with pytest.raises(
        ValueError, match="Сумма углов треугольника " "должна быть равна 180 градусов"
    ):
        Triangle(3, 3, 4, 60, 60, 61)


# Проверка условия существования треугольника
def test_is_triangle_existence():
    triangle = Triangle(3, 4, 5, 90, 53.13, 36.87)

    assert triangle.is_triangle_existence(3, 4, 5) is True
    assert triangle.is_triangle_existence(5, 5, 5) is True
    assert triangle.is_triangle_existence(3, 3, 4) is True

    assert triangle.is_triangle_existence(1, 2, 3) is False
    assert triangle.is_triangle_existence(1, 1, 3) is False
    assert triangle.is_triangle_existence(10, 1, 1) is False


def test_perimeter():
    triangle = Triangle(3, 4, 5, 90, 53.13, 36.87)
    assert triangle.perimeter() == 12

    triangle2 = Triangle(5, 5, 5, 60, 60, 60)
    assert triangle2.perimeter() == 15


def test_area():
    triangle = Triangle(3, 4, 5, 90, 53.13, 36.87)
    assert triangle.area() == 6.0


def test_calculating_height():
    triangle = Triangle(3, 4, 5, 90, 53.13, 36.87)

    # Высота к стороне a (3)
    height_a = triangle.сalculating_height(triangle.a)
    assert abs(height_a - 4.0) < 0.001  # h = 2S/a = 12/3 = 4

    # Высота к стороне b (4)
    height_b = triangle.сalculating_height(triangle.b)
    assert abs(height_b - 3.0) < 0.001  # h = 2S/b = 12/4 = 3


# Определения типа треугольника
def test_triangle_type():

    triangle1 = Triangle(3, 4, 5, 90, 53.13, 36.87)
    assert triangle1.triangle_type(3, 4, 5, 90, 53.13, 36.87) == "Прямоугольный"

    triangle2 = Triangle(5, 5, 5, 60, 60, 60)
    assert triangle2.triangle_type(5, 5, 5, 60, 60, 60) == "Равносторонний"

    triangle3 = Triangle(5, 5, 6, 50, 80, 50)
    assert triangle3.triangle_type(5, 5, 6, 50, 80, 50) == "Равнобедренный"

    triangle4 = Triangle(1, 1, 2**0.5, 90, 45, 45)
    assert (
        triangle4.triangle_type(1, 1, 2**0.5, 90, 45, 45)
        == "Прямоугольный и равнобедренный"
    )

    triangle5 = Triangle(4, 5, 6, 50, 60, 70)
    assert triangle5.triangle_type(4, 5, 6, 50, 60, 70) == "Обычный"
