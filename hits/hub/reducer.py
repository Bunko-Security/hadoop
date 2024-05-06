#!/usr/bin/env python3
import sys

'''
A       auth:0.7559289460184544
B       auth:0.3779644730092272
B       hub:A;0.7559289460184544,1
B       hub:C;0.3779644730092272,1
C       auth:0.3779644730092272
C       hub:A;0.7559289460184544,1
C       hub:D;0.3779644730092272,1
D       auth:0.3779644730092272
D       hub:B;0.3779644730092272,1
'''
lastkey, H = None, {}
new_hub = 0

for line in sys.stdin:
    key, value = line.strip().split('\t')
    name, data = value.strip().split(':')
    
    if lastkey and lastkey != key:
        print(f'{lastkey}\t{",".join(H.get("link")) if H.get("link") else ""}:{H.get("auth")},{new_hub}')
        lastkey, H = key, {}
        new_hub = 0
    else:
        lastkey = key
    
    if name == 'auth':
        H['auth'] = data
    else:
        link, auth = data.strip().split(';')
        if H.get('link'):
            H['link'].append(link)
        else:
            H['link'] = [link]
        new_hub += float(auth)

    
if lastkey:
    print(f'{lastkey}\t{",".join(H.get("link")) if H.get("link") else ""}:{H.get("auth")},{new_hub}')