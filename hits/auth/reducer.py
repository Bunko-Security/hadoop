#!/usr/bin/env python3
import sys

'''
A       hub:1
B       hub:1
A       auth:B;1
C       auth:B;1
C       hub:1
A       auth:C;1
D       auth:C;1
D       hub:1
B       auth:D;1
'''
lastkey, H = None, {}
new_auth = 0

for line in sys.stdin:
    key, value = line.strip().split('\t')
    name, data = value.strip().split(':')
    
    if lastkey and lastkey != key:
        print(f'{lastkey}\t{",".join(H.get("link"))}:{new_auth},{H.get("hub")}')
        lastkey, H = key, {}
        new_auth = 0
    else:
        lastkey = key
    
    if name == 'hub':
        H['hub'] = data
    else:
        link, hub = data.strip().split(';')
        if H.get('link'):
            H['link'].append(link)
        else:
            H['link'] = [link]
        new_auth += float(hub)

    
if lastkey:
    print(f'{lastkey}\t{",".join(H.get("link"))}:{new_auth},{H.get("hub")}')