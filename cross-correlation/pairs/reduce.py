#!/usr/bin/env python3
import sys


(lastkey, summ) = (None, 0)

for line in sys.stdin:
    (key, value) = line.strip().split('\t')
    if lastkey is not None and lastkey != key:
        print(lastkey, '\t', summ, sep='')
        (lastkey, summ) = (key, int(value))
    else:
        (lastkey, summ) = (key, summ + int(value))

if lastkey:
    print(lastkey, '\t', summ, sep='')
