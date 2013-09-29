__author__ = 'Fabianus'

from StringIO import StringIO
import sys
import re

import requests
from Bio import SeqIO


for line in sys.stdin:
    uniprot_id = line.strip()
    url = 'http://www.uniprot.org/uniprot/%s.fasta' % uniprot_id
    req = requests.get(url)
    for rec in SeqIO.parse(StringIO(req.text), 'fasta'):
        seq = str(rec.seq)
        pos = [m.start() for m in re.finditer(r'(?=N[^P][ST][^P])', seq)]
        print uniprot_id
        print seq

        if not pos:
            continue

        print ' '.join(str(x+1) for x in pos)