#!/usr/bin/env python3
import sys
'''
A       :0.7559289460184544,0
B       A,C:0.3779644730092272,1.1338934190276815
C       A,D:0.3779644730092272,1.1338934190276815
D       B:0.3779644730092272,0.3779644730092272
'''

for line in sys.stdin:
    _, value = line.strip().split('\t')
    _, grades = value.strip().split(':')
    _, hub = grades.strip().split(',')
    print('norm_hub', float(hub)**2, sep='\t')