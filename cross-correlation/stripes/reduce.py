#!/usr/bin/env python3
import sys
import json


(lastkey, H) = (None, {})


for line in sys.stdin:
    (key, value) = line.strip().split('\t')
    value: dict = json.loads(value)
    if lastkey is not None and lastkey != key:
        for k, v in H.items():
            print((lastkey, k), '\t', v, sep='')
        
        lastkey = key
        H = value
    else:
        lastkey = key
        for k, v in value.items():
            if H.get(k) is None:
                H[k] = v
            else:
                H[k] += v

if lastkey:
    for k, v in H.items():
        print((lastkey, k), '\t', v, sep='')