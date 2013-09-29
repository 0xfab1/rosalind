__author__ = 'Fabianus'

from Bio.Seq import Seq
import sys

seq = Seq(sys.stdin.read().strip())
print seq.translate()
