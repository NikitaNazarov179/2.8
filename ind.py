#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys

def get_product():
    """""
    Запросить данные о продукте.
    """""
    product = input("Название товара: ")
    shop = input("Магазин: ")
    cost = int(input("Стоимость товара: "))

    # Создать словарь
    return {
        'product': product,
        'shop': shop,
        'cost': cost,
    }


def display_products(products):
    """""
    Отобразить список работников
    """""
    # Проверить что список работников не пуст
    if products:
        # Заголовок таблицы
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "№",
                "Товар",
                "Магазин",
                "Стоимость товара"
            )
        )
        print(line)

        for idx, products in enumerate(products, 1):
            print(
                '| {:^4} | {:<30} | {:<20} | {:<15} |'.format(
                    idx,
                    products.get('product', ''),
                    products.get('shop', ''),
                    products.get('cost', ''),
                    ' ' * 5
                )
            )

        print(line)

    else:
        print("Список товаров пуст.")


def select_product(products, addedtovar):
    """""
    Выбрать необходимый товар
    """""
    result = [product for product in products if product.get('product', '') == addedtovar]
    return result


def main():
    """""
    Главная функция программы
    """""
    print("help - список всех команд")
    # Список товаров
    products = []

    # Организовать бесконечный цикл запроса команд
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            product = get_product()
            products.append(product)

            if len(products) > 1:
                products.sort(key=lambda d: d.get('product', ''))

        elif command == 'list':
            display_products(products)

        elif command == 'select':
            print("Введите товар, информацию о котором хотите получить: ")
            tov = input()
            selected = select_product(products, tov)
            display_products(selected)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить товар;")
            print("list - вывести список товаров;")
            print("select - запросить информацию о товаре;")
            print("help - вывести список команд;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная комманда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()