#!/usr/bin/env python3
import sys

for line in sys.stdin:
    key, value = line.strip().split('\t')
    vertexes, _ = value.strip().split(':')
    print(f'{key}\t{vertexes}:1,1')