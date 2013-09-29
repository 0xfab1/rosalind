__author__ = 'Fabianus'

import sys

k, m, n = [float(x) for x in sys.stdin.read().strip().split(' ')[:3]]

D = k*(k-1+m+n) + m*(k+m-1+n) + n*(k+m+n-1)
print (k*(k-1+2*m+2*n) + 0.75*m*(m-1) + m*n)/D
