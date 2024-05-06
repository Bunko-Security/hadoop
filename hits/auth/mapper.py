#!/usr/bin/env python3
import sys

'''
A   :1,1
B   A,C:1,1
C   A,D:1,1
D   B:1,1
'''

for line in sys.stdin:
    key, value = line.strip().split('\t')
    outgoing, grades = value.strip().split(':')
    auth, hub = grades.strip().split(',')
    print(f'{key}\thub:{hub}')
    if outgoing != '':
        for vertex in outgoing.strip().split(','):
            print(f'{vertex}\tauth:{key};{hub}')