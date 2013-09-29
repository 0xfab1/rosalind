__author__ = 'Fabianus'
import sys

if __name__ == '__main__':
    counts = [0] * 4
    for line in sys.stdin:
        for c in line.strip():
            if c == 'A':
                i = 0
            elif c == 'C':
                i = 1
            elif c == 'G':
                i = 2
            elif c == 'T':
                i = 3
            else:
                i = -1
            if i >= 0:
                counts[i] += 1
    print ' '.join(str(c) for c in counts)
