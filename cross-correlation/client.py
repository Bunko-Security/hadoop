#!/usr/bin/env python3
import argparse

from pyhdfs import HdfsClient


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-H', '--host', type=str, help='Сервер (IP адрес или имя хоста)', default='localhost')
    # parser.add_argument('-P', '--port', type=int, help='Порт', default=50070)
    # parser.add_argument('-U', '--username', type=str, help='Имя пользователя', default='kali')
    # parser.add_argument('alg', choices=['pairs', 'stripes'], help='Алгоритм')
    # parser.add_argument('find_prod', type=str, help='Продукт')
    # args = parser.parse_args()

    # client = HdfsClient(hosts=(args.host + ':' + str(args.port)), user_name=args.username)
    
    # top = {}
    # with client.open(f'/cross-correlation/{args.alg}/part-00000') as file:
    #     for line in file.readlines():
    #         products, count = line.decode('utf-8').strip().split('\t')
    #         prod1, prod2 = products.replace('\'', '').strip('()').split(',')
    #         prod2 = prod2.strip()
    #         if args.find_prod == prod1:
    #             top[prod2] = int(count)
    
    # top = dict(sorted(top.items(), key=lambda item: item[0]))
    
    # top = dict(sorted(top.items(), key=lambda item: item[1], reverse=True))
    
    # number = 1
    # for k, v in top.items():
    #     print(f'Top #{number}: {k} ({v})')
    #     number += 1
    #     if number == 11:
    #         break
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', type=str, help='Сервер (IP адрес или имя хоста)', default='localhost')
    parser.add_argument('-P', '--port', type=int, help='Порт', default=50070)
    parser.add_argument('-U', '--username', type=str, help='Имя пользователя', default='kali')
    parser.add_argument('alg', choices=['pairs', 'stripes'], help='Алгоритм')
    parser.add_argument('find_prod', type=str, help='Продукт')
    args = parser.parse_args()

    client = HdfsClient(hosts=(args.host + ':' + str(args.port)), user_name=args.username)
    
    top = {}
    with client.open(f'/cross-correlation/{args.alg}/part-00000') as file:
        for line in file.readlines():
            products, count = line.decode('utf-8').strip().split('\t')
            prod1, prod2 = products.replace('\'', '').strip('()').split(',')
            prod2 = prod2.strip()
            if args.find_prod == prod1:
                top[prod2] = int(count)
            elif args.find_prod == prod2:
                top[prod1] = int(count)
    
    top = dict(sorted(top.items(), key=lambda item: item[1], reverse=True))
    
    number = 1
    for k, v in top.items():
        print(f'Top #{number}: {k} ({v})')
        number += 1
        if number == 11:
            break
            

if __name__ == '__main__':
    main()
    
