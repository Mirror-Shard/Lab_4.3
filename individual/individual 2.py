#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Создать абстрактный базовый класс Function (функция) с виртуальными методами
вычисления значения функции y = f(x) в заданной точке x и вывода результата на экран.
Определить производные классы Ellipse (эллипс), Hyperbola (гипербола) с собственными
функциями вычисления у в зависимости от входного параметра .
"""
from abc import ABC, abstractmethod


class Function(ABC):
    def __init__(self, a, b, x):
        self.a = a
        self.b = b
        self.x = x
        self.y = 0

    @abstractmethod
    def calculation(self):
        pass


class Ellipse(Function):
    def __init__(self, a, b, x):
        super().__init__(a, b, x)
        self.y = self.calculation()

    def calculation(self):
        a, b, x = self.a, self.b, self.x
        return (b / a) * x


class Hyperbola(Function):
    def __init__(self, a, b, x):
        super().__init__(a, b, x)
        self.y = self.calculation()

    def calculation(self):
        a, b, x = self.a, self.b, self.x
        y = (b / a) * x
        return y, -y


if __name__ == '__main__':
    while True:
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))
        x = int(input("Введите x: "))
        E = Ellipse(a, b, x)
        H = Hyperbola(a, b, x)
        print(f"Для эллипса y равен {E.y}")
        print(f"Для гиперболы y равен {H.y}")
