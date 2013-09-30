__author__ = 'fabi.mulawadi'

import sys

counts = [int(x) for x in sys.stdin.read().strip().split(' ')][:6]
ratios = [1.0, 1.0, 1.0, 0.75, 0.5, 0]

print 2 * sum((p*q) for p, q in zip(counts, ratios))
