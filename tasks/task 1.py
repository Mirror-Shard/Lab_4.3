#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


class Human:
    def __init__(self, id, team):
        self.id = id
        self.team = team


class Hero(Human):
    def __init__(self, id, team):
        super().__init__(id, team)
        self.level = 0
        self.army = []

    def inc_lvl(self, l=1):
        self.level += l


class Soldier(Human):
    def __init__(self, id, team):
        super().__init__(id, team)

    def follow(self, H):
        H.army.append(self.id)


if __name__ == "__main__":
    # Герой команд A и B
    Anton = Hero(1, 'A')
    Boris = Hero(2, 'B')

    # Создаётся армия и рандомно распределяется по героям
    for i in range(3, 13):
        if random.randint(0, 1):
            S = Soldier(i, 'A')
            S.follow(Anton)
        else:
            S = Soldier(i, 'B')
            S.follow(Boris)

    print(f"Армия команды А - {len(Anton.army)} солдат")
    print(f"Армия команды В - {len(Boris.army)} солдат")

    # Увеличение уровня одного из героев в зависимости от их армии
    if len(Anton.army) > len(Boris.army):
        print("Команда А больше, у Антона увеличивается уровень")
        Anton.inc_lvl()
    elif len(Anton.army) < len(Boris.army):
        print("Команда B больше, у Бориса увеличивается уровень")
        Boris.inc_lvl()
    else:
        print("Команды одинаковые")

    # Случайный солдат Антона начинает следовать за ним
    if Anton.army:
        print(f"За Антоном следует солдат №{random.choice(Anton.army)}")
    else:
        print("Команда Антона пуста")
