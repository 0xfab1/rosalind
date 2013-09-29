__author__ = 'Fabianus'

import string
import sys

if __name__ == '__main__':
    table = string.maketrans('ACGTacgt', 'TGCAtgca')
    print string.translate(sys.stdin.read().strip()[::-1], table)
