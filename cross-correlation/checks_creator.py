#!/usr/bin/env python3
import argparse
import pathlib
import random
from pyhdfs import HdfsClient

parser = argparse.ArgumentParser()
parser.add_argument('host', type=str, help='Сервер (IP адрес или имя хоста)')
parser.add_argument('port', type=int, help='Порт')
parser.add_argument('username', type=str, help='Имя пользователя')
parser.add_argument('number_of_checks', type=int, help='Количество чеков')
args = parser.parse_args()

products = ['яйца', 'кетчуп', 'майонез', 'газировка', 'чипсы', 'картошка', 'морковь', 'лук', 'укроп', 'огурец',
            'помидор', 'перец', 'соль', 'вишня', 'орехи', 'виноград', 'сгущенка', 'мука', 'шоколад', 'масло', 'дрожжи',
            'хлеб белый', 'хлеб черный', 'мясо', 'рыба', 'кунжут', 'икра']
            # 'колбаса', 'сыр', 'кукуруза', 'фасоль', 'оливки', 'пельмени', 'лимон', 'чеснок', 'алкоголь', 'ананас',
            # 'креветка', 'крабовые палочки', 'мидии', 'суши', 'гречка', 'вода', 'сок', 'свекла', 'консервы', 'молоко',
            # 'кефир', 'ряженка', 'морская капуста', 'пицца', 'бургер', 'торт', 'печенье',
            # 'пряник', 'конфета', 'зефир', 'пастила', 'леденец', 'жвачка', 'цветок', 'макароны', 'чечевица', 'горох',
            # 'чай черный', 'кофе', 'чай зеленый', 'сахар', 'груша', 'часы', 'телефон', 'банан', 'мандарин',
            # 'апельсин', 'мяч', 'нож', 'ложка', 'вилка', 'стакан', 'тарелка', 'банка',
            # 'кастрюля', 'сковорода', 'перепелиное яйцо', 'капли для глаз', 'увлажняющая мазь',
            # 'средство для мытья посуды', 'перчатки', 'увлажнитель воздуха', 'вентилятор', 'освежитель воздуха', 'морс',
            # 'очки', 'шаурма', 'тапочки', 'полотенце', 'гель для душа', 'антиперспирант', 'чемодан', 'яблоко']

client = HdfsClient(hosts=(args.host + ':'+ str(args.port)), user_name=args.username)
client.delete('/cross-correlation/input/', recursive=True)
for i in range(args.number_of_checks):
    check_length = random.randint(6, 20)
    check = ';'.join(random.sample(products, check_length))  # Maybe just random.randit
    filename = f'check_{i + 1}.txt'
    with open(filename, 'w+', encoding='utf-8') as f:
        f.write(check)
    client.copy_from_local(filename, '/cross-correlation/input/' + filename)
    pathlib.Path.cwd().joinpath(filename).unlink()
