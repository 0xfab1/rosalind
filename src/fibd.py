__author__ = 'fabianus'

import numpy as np

n = 94  # the question is how many rabbits in month n
m = 20  # rabbit lifespan (months)
k = 1  # how many pairs of children born to every reproductive pair

wabbits = np.zeros(m, dtype='object')  # use python number to avoid integer overflow
wabbits[0] = 1  # start with 1 pair of rabbit in month 1

rates = np.zeros((m, m), dtype='object')
for i in xrange(m - 1):
    rates[i, i + 1] = 1  # rabbits do not survive beyond m month

rates[1:, 0] = k  # after 2 months, rabbits start reproducing

print np.sum(wabbits.dot(np.linalg.matrix_power(rates, n - 1)))