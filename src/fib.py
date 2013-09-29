__author__ = 'Fabianus'

import sys

n, k = sys.stdin.read().split(' ')
n, k = int(n), int(k)

count = [1, 1]
for i in xrange(n-2):
    count.append(count[-2] * k + count[-1])

print count[-1]