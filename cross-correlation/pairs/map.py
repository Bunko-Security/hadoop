#!/usr/bin/python3
import sys


for line in sys.stdin:
    items = line.strip().split(' ')
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                print((item1, item2), '\t1')


# for line in sys.stdin:
#     items = line.strip().split(' ')
#     items.sort()
#     for index1, item1 in enumerate(items):
#         for index2, item2 in enumerate(items):
#             if index2 > index1:
#                 print((item1, item2), '\t1', sep='')