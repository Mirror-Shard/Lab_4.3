#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Triangle с полями-сторонами. Определить методы изменения сторон,
вычисления углов, вычисления периметра. Создать производный класс RightAngled
(прямоугольный), имеющий поле площади. Определить метод вычисления площади.
"""
from math import sqrt, acos


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.__check()

    def change_side(self, a=0, b=0, c=0):
        if not a or b or c:
            a = int(input("Введите сторону А:"))
            b = int(input("Введите сторону B:"))
            c = int(input("Введите сторону C:"))
        self.a, self.b, self.c = a, b, c
        self.__check()

    def perimeter(self):
        return self.a + self.b + self.c

    def angles(self):
        a, b, c = self.a, self.b, self.c
        aa = acos((b**2 + c**2 - a**2) / (2*b*c))
        bb = acos((a**2 + c**2 - b**2) / (2*a*c))
        cc = acos((a**2 + b**2 - c**2) / (2*a*b))
        return round(aa, 3), round(bb, 3), round(cc, 3)

    def __check(self):
        a, b, c = self.a, self.b, self.c
        if a+b < c or a+c < b or b+c < a:
            print("Треугольник не существует")
            self.change_side()

# Добавить проверку прямоугольнисти
class RightAngled(Triangle):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.__rcheck()
        self.area = self.__area_calculating()

    def __rcheck(self):
        a, b, c = self.a, self.b, self.c
        if (a * a + b * b == c * c) or (c * c + b * b == a * a) or (a * a + c * c == b * b):
            print("Треугольник является прямоугольным")
        else:
            print("Прямоугольник не является прямоугольным")
            self.change_side()

    def __area_calculating(self):
        a, b, c = self.a, self.b, self.c
        a = min(a, b)
        b = min(b, c)
        return a * b / 2


if __name__ == '__main__':
    while True:
        a = int(input("Введите сторону А:"))
        b = int(input("Введите сторону B:"))
        c = int(input("Введите сторону C:"))
        TR = RightAngled(a, b, c)
        print(f"Периметр треугольника {TR.perimeter()}")
        print(f"Углы треугольника {TR.angles()}")
        print(f"Площадь треугольника {TR.area}")
