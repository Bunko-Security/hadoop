#!/usr/bin/env python3
import sys
'''
A       B,C:2.0,1
B       D:1.0,1
C       B:1.0,1
D       C:1.0,1

2.6457513110645907
'''

norm_auth = float(sys.argv[1])

for line in sys.stdin:
    key, value = line.strip().split('\t')
    incoming, grades = value.strip().split(':')
    auth, hub = grades.strip().split(',')
    
    auth = float(auth) / norm_auth
    print(f'{key}\t{incoming}:{auth},{hub}')