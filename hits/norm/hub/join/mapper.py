#!/usr/bin/env python3
import sys
'''
A       :0.7559289460184544,0
B       A,C:0.3779644730092272,1.1338934190276815
C       A,D:0.3779644730092272,1.1338934190276815
D       B:0.3779644730092272,0.3779644730092272

1.6475089420958278
'''

norm_hub = float(sys.argv[1])

for line in sys.stdin:
    key, value = line.strip().split('\t')
    incoming, grades = value.strip().split(':')
    auth, hub = grades.strip().split(',')
    
    hub = float(hub) / norm_hub
    print(f'{key}\t{incoming}:{auth},{hub}')