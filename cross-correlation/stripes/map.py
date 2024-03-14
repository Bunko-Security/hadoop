#!/usr/bin/env python3
import sys
import json

for line in sys.stdin:
    items = line.strip().split(' ')
    for item1 in items:
        H = {}
        for item2 in items:
            if item1 != item2:
                if H.get(item2) is None:
                    H[item2] = 1
                else:
                    H[item2] += 1
        print(item1, '\t', json.dumps(H))
        

# for line in sys.stdin:
#     items = line.strip().split(' ')
#     items.sort()
#     for index1, item1 in enumerate(items):
#         H = {}
#         for index2, item2 in enumerate(items):
#             if index2 > index1:
#                 if H.get(item2) is None:
#                     H[item2] = 1
#                 else:
#                     H[item2] += 1
#         print(item1, '\t', json.dumps(H), sep='')