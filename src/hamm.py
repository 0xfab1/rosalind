__author__ = 'Fabianus'

import sys

s, t = sys.stdin.read().strip().split('\n')[:2]
print sum(0 if p==q else 1 for p,q in zip(s,t))