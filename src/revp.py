__author__ = 'Fabianus'

from Bio import SeqIO
import sys
from revc import revc


def check_revp(seq, pos, k):
    return seq[pos-k:pos] == revc(seq[pos:pos+k])


if __name__ == '__main__':
    start, stop = 4, 12
    for rec in SeqIO.parse(sys.stdin, 'fasta'):
        seq = str(rec.seq)
        positions = range(start/2, len(seq)-start/2+1)

        results = {}
        for k in xrange(start, stop+1, 2):
            result = []
            for pos in positions:
                if check_revp(seq, pos, k/2):
                    result.append(pos)
            positions = results[k] = result

        for p, q in sorted((v-k/2+1, k) for k, vs in results.iteritems() for v in vs):
            print p, q