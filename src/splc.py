__author__ = 'Fabianus'

import sys
from Bio import SeqIO
from Bio.Seq import Seq

parse = SeqIO.parse(sys.stdin, 'fasta')

main_seq = str(parse.next().seq)

for rec in parse:
    seq = str(rec.seq)
    main_seq = main_seq.replace(seq, '')

print Seq(main_seq).translate()