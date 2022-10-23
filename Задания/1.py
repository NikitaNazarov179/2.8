#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def test():
    a = int(input("Введите число: "))
    if a < 0:
        negative()
    elif a >= 0:
        positive()

def negative():
    print("Число отрицательное")

def positive():
    print("Число положительное")

if __name__ == '__main__':
    test()