__author__ = 'Fabianus'

import string
import sys

_table = string.maketrans('ACGTacgt', 'TGCAtgca')
def revc(seq):
    return string.translate(seq[::-1], _table)


if __name__ == '__main__':
    print revc(sys.stdin.read().strip())
