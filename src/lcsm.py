__author__ = 'Fabianus'

import sys

import numpy as np
from Bio import SeqIO


def make_matrix(s, t):
    ls, lt = len(s), len(t)
    mat = np.zeros((ls + 1, lt + 1), dtype=int)

    for i in xrange(1, ls + 1):
        for j in xrange(1, lt + 1):
            mat[i][j] = mat[i - 1][j - 1] + 1 if s[i - 1] == t[j - 1] else 0
    return mat


def lcs(s, t):
    result = set()
    mat = make_matrix(s, t)
    for row, col in np.argwhere(mat == np.amax(mat)):
        v = mat[row, col]
        result.add(s[row - v:row])
    return list(result)


if __name__ == '__main__':
    result = None
    for rec in SeqIO.parse(sys.stdin, 'fasta'):
        seq = str(rec.seq)
        if result is None:
            result = [seq]
        else:
            tmp = [lcs(p, seq) for p in result]
            result = [item for sublist in tmp for item in sublist]  # flatten

    result = sorted(result, key=lambda x: len(x), reverse=True)
    print '\n'.join(result)