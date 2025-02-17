

# This file was *autogenerated* from the file solve-1.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_15000 = Integer(15000); _sage_const_65537 = Integer(65537); _sage_const_7 = Integer(7); _sage_const_4 = Integer(4); _sage_const_16 = Integer(16); _sage_const_3 = Integer(3); _sage_const_6 = Integer(6); _sage_const_1000 = Integer(1000)# https://facthacks.cr.yp.to/batchgcd.html
from tqdm import tqdm
from datetime import datetime
import time

def log(msg, important=False):
    t = datetime.fromtimestamp(time.time())
    print(f'[{"*" if important else " "}] {t} | {msg}')

def producttree(X):
    result = [X]
    while len(X) > _sage_const_1 :
        log(f'Start computing product tree: {len(X)}')
        X = [prod(X[i*_sage_const_2 :(i+_sage_const_1 )*_sage_const_2 ]) for i in range((len(X)+_sage_const_1 )//_sage_const_2 )]
        result.append(X)
        log(f'Finish computing product tree: {len(X)}')
    return result

def batchgcd_faster(X):
    prods = producttree(X)
    R = prods.pop()
    while prods:
        X = prods.pop()
        log(f'Start computing remainder tree: {len(X)}')
        R = [R[floor(i//_sage_const_2 )] % X[i]**_sage_const_2  for i in range(len(X))]
        log(f'Finish computing remainder tree: {len(X)}')
    return [gcd(r//n,n) for r,n in zip(R,X)]

with open('transcript.log') as f:
    lines = f.readlines()

ns = []
for i in tqdm(range(_sage_const_15000 )):
    n = gcd(
        _sage_const_2 **_sage_const_65537  - int(lines[_sage_const_7 *i+_sage_const_4 ], _sage_const_16 ),
        _sage_const_3 **_sage_const_65537  - int(lines[_sage_const_7 *i+_sage_const_6 ], _sage_const_16 ),
    )
    ns.append(int(n))

t1 = time.time()
gcds = batchgcd_faster(ns)
t2 = time.time()
log(f'Time elapsed: {t2-t1}s')

for i, g in enumerate(gcds):
    if g < _sage_const_1000 : continue
    n = ns[i]
    log('Small factor:')
    log(f'-> n = {ns[i]}', important=True)
    log(f'-> g = {g}', important=True)
    log(f'-> encrypted_secret = {int(lines[7*i+8], 16)}', important=True)

'''
Experiment:
4096 1024-bit numbers: 66.42s
8192 1024-bit numbers: 272.30s
'''

