#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import math
import sys

def cylinder():

    while True:
        vs = int(input("Боковая или полная? (введите число):\n"
                       "1 -> Боковая\n"
                       "2 -> Полная\n"
                       ">>> "))
        if (vs != 1) and (vs != 2):
            print(f"Неизвестная комманда {vs}", file=sys.stderr)
            break

        r = int(input("Введите радиус "))
        h = int(input("Введите высоту цилиндра: "))

        if vs == 1:
            s = 2 * math.pi * r * h
            print("S боковая = ", '{:.3f}'.format(s))
            break

        elif vs == 2:
            s = (2 * math.pi * r * h) + (circle(r) * 2)
            print("S полная = ", '{:.3f}'.format(s))
            break

def circle(r):

    return math.pi * (r ** 2)

if __name__ == '__main__':
    cylinder()