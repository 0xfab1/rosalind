__author__ = 'Fabianus'

import string
import sys

if __name__ == '__main__':
    table = string.maketrans('Tt', 'Uu')
    print string.translate(sys.stdin.read().strip(), table)