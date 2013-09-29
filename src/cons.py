__author__ = 'Fabianus'

import sys
from Bio import SeqIO

counts = [None] * 4
index = dict(A=0, C=1, G=2, T=3)

for rec in SeqIO.parse(sys.stdin, 'fasta'):
    seq = str(rec.seq)
    for i, c in enumerate(seq):
        x = index[c]
        if not counts[x]:
            counts[x] = [0] * len(seq)
        counts[x][i] += 1

cons = []
for i in xrange(len(counts[0])):
    maxval = idx = -1
    for j in xrange(4):
        count = counts[j][i]
        if count > maxval:
            maxval, idx = count, j
    cons.append(idx)

print ''.join('ACGT'[x] for x in cons)
for i, c in enumerate('ACGT'):
    print '%s: %s' % (c, ' '.join(str(x) for x in counts[i]))
