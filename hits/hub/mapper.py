#!/usr/bin/env python3
import sys
'''
A       B,C:0.7559289460184544,1
B       D:0.3779644730092272,1
C       B:0.3779644730092272,1
D       C:0.3779644730092272,1
'''

for line in sys.stdin:
    key, value = line.strip().split('\t')
    outgoing, grades = value.strip().split(':')
    auth, hub = grades.strip().split(',')
    print(f'{key}\tauth:{auth}')
    if outgoing != '':
        for vertex in outgoing.strip().split(','):
            print(f'{vertex}\thub:{key};{auth}')