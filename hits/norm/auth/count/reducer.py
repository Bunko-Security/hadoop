#!/usr/bin/env python3
import sys
import math

'''
norm_auth       4.0
norm_auth       1.0
norm_auth       1.0
norm_auth       1.0
'''

norm_auth = 0.0
for line in sys.stdin:
    _, value = line.strip().split('\t')
    norm_auth += float(value)

print(math.sqrt(norm_auth))