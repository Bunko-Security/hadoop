#!/usr/bin/env python3
import sys
import math

'''
norm_hub        0.0
norm_hub        1.2857142857142854
norm_hub        1.2857142857142854
norm_hub        0.14285714285714282
'''

norm_auth = 0.0
for line in sys.stdin:
    _, value = line.strip().split('\t')
    norm_auth += float(value)

print(math.sqrt(norm_auth))