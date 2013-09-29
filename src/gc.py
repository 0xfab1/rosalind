__author__ = 'Fabianus'

import sys

from Bio.SeqUtils import GC
from Bio import SeqIO

top = (0, None)
for rec in SeqIO.parse(sys.stdin, 'fasta'):
    gc = GC(rec.seq)
    if gc > top[0]:
        top = (gc, rec)

print '%s\n%s' % (top[1].name, top[0])