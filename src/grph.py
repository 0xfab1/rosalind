__author__ = 'Fabianus'

import sys

from Bio import SeqIO

k = 3
seqs = {}

G = {}
for rec in SeqIO.parse(sys.stdin, 'fasta'):
    myname, myseq = rec.name, rec.seq
    myprefix, mysuffix = str(myseq[:k]), str(myseq[-k:])

    seqs[myname] = (myprefix, mysuffix)

    incoming = []
    outgoing = []
    for name in G.iterkeys():
        prefix, suffix = seqs[name]
        if myprefix == suffix:
            incoming.append(name)
        if mysuffix == prefix:
            outgoing.append(name)

    G[myname] = outgoing
    for name in incoming:
        G[name].append(myname)

for name, targets in G.iteritems():
    for t in targets:
        print '%s %s' % (name, t)