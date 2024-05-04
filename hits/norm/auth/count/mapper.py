#!/usr/bin/env python3
import sys
'''
A       B,C:2.0,1
B       D:1.0,1
C       B:1.0,1
D       C:1.0,1
'''

for line in sys.stdin:
    _, value = line.strip().split('\t')
    _, grades = value.strip().split(':')
    auth, _ = grades.strip().split(',')
    print('norm_auth', float(auth)**2, sep='\t')